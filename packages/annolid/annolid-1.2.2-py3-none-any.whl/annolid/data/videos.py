import os
import glob
import sys
import heapq
import cv2
import numpy as np
import random
import subprocess
from typing import Generator, List
from pathlib import Path
from collections import deque
from annolid.segmentation.maskrcnn import inference

try:
    import decord as de
    IS_DECORD_INSTALLED = True
except ImportError:
    IS_DECORD_INSTALLED = False
    print("Decord is not installed.")


def get_video_files(video_folder):
    """
    Retrieves a list of video files from the specified folder.

    Parameters:
    video_folder (str or Path): Path to the folder containing video files.

    Returns:
    list: A list of paths to video files found in the specified folder.

    Supported video formats: .mp4, .avi, .mov, .mkv, .flv, .wmv, .mpg, .mpeg
    """
    video_extensions = ['*.mp4', '*.avi', '*.mov',
                        '*.mkv', '*.flv', '*.wmv', '*.mpg', '*.mpeg']
    video_files = []
    for ext in video_extensions:
        video_files.extend(glob.glob(os.path.join(video_folder, ext)))
    return video_files


def frame_from_video(video, num_frames):
    attempt = 0
    for i in range(num_frames):
        success, frame = video.read()
        if success:
            yield frame
        else:
            attempt += 1
            if attempt >= 2000:
                break
            else:
                video.set(cv2.CAP_PROP_POS_FRAMES, i+1)
                print('Cannot read this frame:', i)
                continue


def test_cmd(cmd):
    """Test the cmd.
    Modified from moviepy 
    """
    try:
        popen_params = {
            "stdout": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "stdin": subprocess.DEVNULL
        }
        # to remove unwanted window on windows
        # when created the child process
        if os.name == "nt":
            popen_params["creationflags"] = 0x08000000

        proc = subprocess.Popen(cmd, **popen_params)
        proc.communicate()
    except Exception as err:
        return False, err
    else:
        return True, None


def get_ffmpeg_path():
    """Test and find the correct ffmpeg binary file.
    Modified from moviepy.
    """
    ffmpeg_binary = os.getenv('FFMPEG_BINARY', 'ffmpeg-imageio')
    if ffmpeg_binary == 'ffmpeg-imageio':
        from imageio.plugins.ffmpeg import get_exe
        ffmpeg_binary = get_exe()
    elif ffmpeg_binary == 'auto-detect':
        if test_cmd(['ffmpeg'])[0]:
            ffmpeg_binary = 'ffmpeg'
        elif test_cmd(['ffmpeg.exe'])[0]:
            ffmpeg_binary = 'ffmpeg.exe'
        else:
            ffmpeg_binary = 'unset'
    else:
        success, err = test_cmd([ffmpeg_binary])
        if not success:
            raise IOError(
                str(err) +
                " - The path specified for the ffmpeg binary might be wrong")
    return ffmpeg_binary


def ffmpeg_extract_subclip(filename, t1, t2, targetname=None):
    """ 
     Makes a new video file playing video file ``filename`` between
        the times ``t1`` and ``t2``.
    Modified from moviepy ffmpeg_tools
    """
    name, ext = os.path.splitext(filename)
    if not targetname:
        T1, T2 = [int(1000*t) for t in [t1, t2]]
        targetname = "%sSUB%d_%d.%s" % (name, T1, T2, ext)

    ffmpeg_binary = get_ffmpeg_path()
    cmd = [ffmpeg_binary, "-y",
           "-ss", "%0.2f" % t1,
           "-i", filename,
           "-t", "%0.2f" % (t2-t1),
           "-vcodec", "copy",
           "-acodec", "copy", "-strict", "-2", targetname]

    popen_params = {"stdout": subprocess.DEVNULL,
                    "stderr": subprocess.PIPE,
                    "stdin": subprocess.DEVNULL}

    if os.name == "nt":
        popen_params["creationflags"] = 0x08000000

    proc = subprocess.Popen(cmd, **popen_params)

    out, err = proc.communicate()
    proc.stderr.close()

    if proc.returncode:
        raise IOError(err.decode('utf8'))
    del proc


def extract_subclip(video_file,
                    start_time,
                    end_time):
    video_dir = Path(video_file).parent
    out_video_name = Path(video_file).stem + \
        f"_{str(start_time)}_{str(end_time)}.mp4"
    out_video_path = video_dir / out_video_name

    ffmpeg_extract_subclip(
        video_file,
        start_time,
        end_time,
        targetname=str(out_video_path))

    return str(out_video_path)


def key_frames(video_file=None,
               out_dir=None,
               ctx=None,
               sub_clip=False,
               start_seconds=None,
               end_seconds=None,
               ):

    if sub_clip and start_seconds is not None and end_seconds is not None:
        video_file = extract_subclip(video_file,
                                     start_seconds,
                                     end_seconds)

    vr = de.VideoReader(video_file)
    key_idxs = vr.get_key_indices()

    video_name = Path(video_file).stem
    video_name = video_name.replace(' ', '_')
    if out_dir is None:
        out_dir = Path(video_file).parent / video_name
        out_dir = out_dir.with_suffix('')
    out_dir = Path(out_dir)
    out_dir.mkdir(
        parents=True,
        exist_ok=True)
    for ki in key_idxs:
        frame = vr[ki].asnumpy()
        out_frame_file = out_dir / \
            f"{(video_name).replace(' ','_')}_{ki:08}.png"
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imwrite(str(out_frame_file), frame)
        print(f"Saved {str(out_frame_file)}")
    print(f"Please check your frames located at {out_dir}")
    return out_dir


def video_loader(video_file=None):
    if not Path(video_file).exists:
        return
    with open(video_file, 'rb') as f:
        vr = de.VideoReader(f, ctx=de.cpu(0))
    return vr


class CV2Video:
    def __init__(self, video_file, use_decord=False):
        self.video_file = Path(video_file).resolve()
        if IS_DECORD_INSTALLED:
            self.reader = de.VideoReader(str(self.video_file))
        else:
            self.reader = None
            self.cap = cv2.VideoCapture(str(self.video_file))
        self.current_frame_timestamp = None
        self.width = None
        self.height = None
        self.first_frame = None
        self.fps = None

    def get_first_frame(self):
        if self.first_frame is None:
            self.first_frame = self.load_frame(0)
        return self.first_frame

    def get_width(self):
        if self.width is None:
            self.width = self.first_frame.shape[1]
        return self.width

    def get_height(self):
        if self.height is None:
            self.height = self.first_frame.shape[0]
        return self.height

    def get_fps(self):
        if self.reader is not None:
            self.fps = self.reader.get_avg_fps()
        else:
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        return self.fps

    def load_frame(self, frame_number):
        if self.reader is not None:
            frame = self.reader[frame_number].asnumpy()
        else:
            if self.cap.get(cv2.CAP_PROP_POS_FRAMES) != frame_number:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
                self.current_frame_timestamp = self.cap.get(
                    cv2.CAP_PROP_POS_MSEC)
            ret, frame = self.cap.read()

            if not ret or frame is None:
                raise KeyError(f"Cannot load frame number: {frame_number}")

            # convert bgr to rgb
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        return frame

    def get_time_stamp(self):
        return self.current_frame_timestamp

    def total_frames(self):
        if self.reader is not None:
            return len(self.reader)
        else:
            return int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def get_frames_in_batches(self, start_frame: int,
                              end_frame: int,
                              batch_size: int) -> Generator[np.ndarray, None, None]:
        """
        Retrieves frames in batches between start and end frames.

        Args:
            start_frame (int): The starting frame number.
            end_frame (int): The ending frame number.
            batch_size (int): The size of each batch.

        Yields:
            np.ndarray: A batch of video frames.
        """
        if start_frame >= end_frame:
            raise ValueError("Start frame must be less than end frame.")

        total_frames = self.total_frames()
        end_frame = min(end_frame, total_frames)

        if end_frame - start_frame < batch_size:
            batch_size = end_frame - start_frame

        for batch_start in range(start_frame, end_frame, batch_size):
            batch_end = min(batch_start + batch_size, end_frame)
            for frame_number in range(batch_start, batch_end):
                yield self.load_frame(frame_number)

    def get_frames_between(self, start_frame: int,
                           end_frame: int) -> List[np.ndarray]:
        """
        Retrieves all frames between start and end frames.

        Args:
            start_frame (int): The starting frame number.
            end_frame (int): The ending frame number.

        Returns:
            List[np.ndarray]: A list of video frames.
        """
        if start_frame >= end_frame:
            raise ValueError("Start frame must be less than end frame.")

        total_frames = self.total_frames()
        end_frame = min(end_frame, total_frames)

        frames = []
        for frame_number in range(start_frame, end_frame):
            frames.append(self.load_frame(frame_number))

        return np.stack(frames)


def extract_frames(video_file='None',
                   num_frames=100,
                   out_dir=None,
                   show_flow=False,
                   algo='flow',
                   keep_first_frame=False,
                   sub_clip=False,
                   start_seconds=None,
                   end_seconds=None,
                   prediction=True
                   ):
    """
    Extract frames from the given video file. 
    This function saves the wanted number of frames based on
    optical flow by default.
    Or you can save all the frames by providing `num_frames` = -1. 

    """

    if sub_clip and start_seconds is not None and end_seconds is not None:
        video_file = extract_subclip(video_file,
                                     start_seconds,
                                     end_seconds)

    video_name = os.path.splitext(os.path.basename(video_file))[0]
    video_name = video_name.replace(' ', '_')
    if out_dir is None:
        out_dir = os.path.splitext(video_file)[0]
    else:
        out_dir = os.path.join(out_dir, video_name)

    # add extracting methods to folder name
    out_dir = f"{out_dir}_{algo}"

    if not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    if algo == 'keyframes':
        out_dir = key_frames(video_file, out_dir,
                             sub_clip=sub_clip,
                             start_seconds=start_seconds,
                             end_seconds=end_seconds)
        yield 100, f"Done. Frames located at {out_dir}."

    cap = cv2.VideoCapture(video_file)
    n_frames = int(cap.get(7))

    current_frame_number = int(cap.get(1))

    subtractor = cv2.createBackgroundSubtractorMOG2()
    keeped_frames = []

    ret, old_frame = cap.read()

    if keep_first_frame:
        # save the first frame
        out_frame_file = f"{out_dir}{os.sep}{video_name}_{current_frame_number:08}.png"
        cv2.imwrite(out_frame_file, old_frame)

    if num_frames < -1 or num_frames > n_frames:
        print(f'The video has {n_frames} number frames in total.')
        print('Please input a valid number of frames!')
        return
    elif num_frames == 1:
        print(f'Please check your first frame here {out_dir}')
        return
    elif num_frames > 2:
        # if save the first frame and the last frame
        # so to make the number of extract frames
        # as the user provided exactly
        if keep_first_frame:
            num_frames -= 1

    hsv = np.zeros_like(old_frame)
    hsv[..., 1] = 255

    # keeped frame index
    ki = 0

    while ret:

        frame_number = int(cap.get(1))
        ret, frame = cap.read()

        progress_percent = ((frame_number + 1) / n_frames) * 100

        if num_frames == -1:
            out_frame_file = f"{out_dir}{os.sep}{video_name}_{frame_number:08}.png"
            if ret:
                cv2.imwrite(
                    out_frame_file, frame)
                print(f'Saved the frame {frame_number}.')
            continue
        if algo == 'random' and num_frames != -1:
            if ret:
                if len(keeped_frames) < num_frames:
                    keeped_frames.append((ki,
                                          frame_number,
                                          frame))
                else:
                    j = random.randrange(ki + 1)
                    if j < num_frames:
                        keeped_frames[j] = ((j,
                                             frame_number,
                                             frame))
                ki += 1
                yield progress_percent, f'Processed {ki} frames.'
            continue
        if algo == 'flow' and num_frames != -1:
            mask = subtractor.apply(frame)
            old_mask = subtractor.apply(old_frame)

            out_frame = cv2.bitwise_and(frame, frame, mask=mask)
            old_out_frame = cv2.bitwise_and(
                old_frame, old_frame, mask=old_mask)
            try:
                out_frame = cv2.cvtColor(out_frame, cv2.COLOR_BGR2GRAY)
                old_out_frame = cv2.cvtColor(old_out_frame, cv2.COLOR_BGR2GRAY)

                flow = cv2.calcOpticalFlowFarneback(
                    old_out_frame, out_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)

                if show_flow:
                    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
                    hsv[..., 0] = ang*180/np.pi/2
                    hsv[..., 2] = cv2.normalize(
                        mag, None, 0, 255, cv2.NORM_MINMAX)
                    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

                q_score = int(np.abs(np.sum(flow.reshape(-1))))
                progress_msg = f"precessing frame {frame_number},the diff to prev frame is {q_score}."

                if len(keeped_frames) < num_frames:
                    heapq.heappush(
                        keeped_frames, ((q_score, frame_number, frame)))
                else:
                    heapq.heappushpop(
                        keeped_frames, ((q_score, frame_number, frame)))

                if show_flow:
                    cv2.imshow("Frame", rgb)
                yield progress_percent, progress_msg
            except:
                print('skipping the current frame.')

            old_frame = frame
        key = cv2.waitKey(1)
        if key == 27:
            break

    for kf in keeped_frames:
        s, f, p = kf
        out_img = f"{out_dir}{os.sep}{video_name}_{f:08}_{s}.png"
        cv2.imwrite(out_img, p)
        # default mask rcnn prediction if select less than 5 frames
        if prediction and num_frames <= 5:
            try:
                inference.predict_mask_to_labelme(out_img, 0.7)
            except:
                print("Please install pytorch and torchvision as follows.")
                print("pip install torch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0")
                pass

    cap.release()
    cv2.destroyAllWindows()
    yield 100, f"Done. Frames located at {out_dir}"


def track(video_file=None,
          name="YOLOV5",
          weights=None
          ):

    points = [deque(maxlen=30) for _ in range(1000)]

    if name == "YOLOV5":
        # avoid installing pytorch
        # if the user only wants to use it for
        # extract frames
        # maybe there is a better way to do this
        sys.path.append("detector/yolov5/")
        import torch
        from annolid.detector.yolov5.detect import detect
        from annolid.utils.config import get_config
        cfg = get_config("./configs/yolov5s.yaml")
        from annolid.detector.yolov5.utils.general import strip_optimizer

        opt = cfg
        if weights is not None:
            opt.weights = weights
        opt.source = video_file

        with torch.no_grad():
            if opt.update:  # update all models (to fix SourceChangeWarning)
                for opt.weights in ['yolov5s.pt', 'yolov5m.pt', 'yolov5l.pt', 'yolov5x.pt']:
                    detect(opt, points=points)
                    strip_optimizer(opt.weights)
            else:
                detect(opt, points=points)
                strip_optimizer(opt.weights)
    else:
        from annolid.tracker.build_deepsort import build_tracker
        from annolid.detector import build_detector
        from annolid.utils.draw import draw_boxes
        if not (os.path.isfile(video_file)):
            print("Please provide a valid video file")
        detector = build_detector()
        class_names = detector.class_names

        cap = cv2.VideoCapture(video_file)

        ret, prev_frame = cap.read()
        deep_sort = build_tracker()

        while ret:
            ret, frame = cap.read()
            if not ret:
                print("Finished tracking.")
                break
            im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            bbox_xywh, cls_conf, cls_ids = detector(im)
            bbox_xywh[:, 3:] *= 1.2
            mask = cls_ids == 0
            cls_conf = cls_conf[mask]

            outputs = deep_sort.update(bbox_xywh, cls_conf, im)

            if len(outputs) > 0:
                bbox_xyxy = outputs[:, :4]
                identities = outputs[:, -1]
                frame = draw_boxes(frame,
                                   bbox_xyxy,
                                   identities,
                                   draw_track=True,
                                   points=points
                                   )

            cv2.imshow("Frame", frame)

            key = cv2.waitKey(1)
            if key == 27:
                break

            prev_frame = frame

        cv2.destroyAllWindows()
        cap.release()


def extract_video_metadata(cap):
    """Extract video metadata

    Args:
        cap (VideoCapture): cv2 VideoCapture object

    Returns:
        dict : dict of video metadata
    """
    meta_data = {
        'frame_width': cap.get(cv2.CAP_PROP_FRAME_WIDTH),
        'frame_height': cap.get(cv2.CAP_PROP_FRAME_HEIGHT),
        'fps': cap.get(cv2.CAP_PROP_FPS),
        'format': cap.get(cv2.CAP_PROP_FORMAT),
        'frame_count': cap.get(cv2.CAP_PROP_FRAME_COUNT),
        'fourcc': cap.get(cv2.CAP_PROP_FOURCC),
        'mode': cap.get(cv2.CAP_PROP_MODE)
    }
    return meta_data


def extract_frames_from_videos(input_folder, output_folder=None, num_frames=5):
    """
    Extract specified number of frames from each video in the folder and save as PNG files.

    Args:
        input_folder (str): Path to the folder containing video files.
        output_folder (str): Path to the folder to save extracted frames. Defaults to './extracted_frames'.
        num_frames (int): Number of frames to extract. Defaults to 5.
    """
    # Set default output folder if not provided
    if output_folder is None:
        output_folder = os.path.join(os.getcwd(), "extracted_frames")

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all video files in the input folder
    for video_file in os.listdir(input_folder):
        video_path = os.path.join(input_folder, video_file)
        if not video_file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.mpg')):
            continue  # Skip non-video files

        # Open the video
        cap = cv2.VideoCapture(video_path)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if frame_count < 1:
            print(f"Skipping {video_file}: Unable to determine frame count.")
            cap.release()
            continue

        indices = []
        if frame_count >= num_frames:
            indices = [int(i * (frame_count - 1) / (num_frames - 1))
                       for i in range(num_frames)]
        elif frame_count > 0:  # Handle edge case for short videos
            indices = list(range(frame_count))
        else:
            print(f"Skipping {video_file}: No frames found.")
            continue

        # Determine the frame indices to extract
        if num_frames == 1:
            indices = [frame_count // 2]
        else:
            indices = [int(i * (frame_count - 1) / (num_frames - 1))
                       for i in range(num_frames)]

        # Extract frames and save as PNG
        for idx in indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            if ret:
                frame_filename = f"{os.path.splitext(video_file)[0]}_frame{idx}.png"
                frame_path = os.path.join(output_folder, frame_filename)
                cv2.imwrite(frame_path, frame)
            else:
                print(f"Warning: Failed to read frame {idx} from {video_file}")

        cap.release()
