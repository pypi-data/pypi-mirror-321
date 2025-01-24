import glob
import cv2
import numpy as np
import torch
import pandas as pd
import queue
from pathlib import Path
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import ColorMode, Visualizer
from detectron2 import model_zoo
from detectron2.data.datasets import register_coco_instances
from detectron2.data.datasets import builtin_meta
from detectron2.data import get_detection_dataset_dicts
from annolid.postprocessing.quality_control import pred_dict_to_labelme
import pycocotools.mask as mask_util
from annolid.annotation.keypoints import save_labels
from annolid.postprocessing.quality_control import TracksResults
from annolid.annotation.masks import mask_iou
from annolid.data.videos import key_frames
from torchvision.ops import nms
from annolid.data import videos


class Segmentor():
    """
    Class for training and inferencing Mask-RCNN based models.
    """

    def __init__(self,
                 dataset_dir=None,
                 model_pth_path=None,
                 score_threshold=0.15,
                 overlap_threshold=0.95,
                 model_config=None,
                 num_instances_per_class=1
                 ) -> None:
        self.dataset_dir = dataset_dir
        self.score_threshold = score_threshold
        self.overlap_threshold = overlap_threshold

        if model_config is None:
            model_config = "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"

        dataset_name = Path(self.dataset_dir).stem
        self.subject_queue = queue.PriorityQueue(3)
        self.left_object_queue = queue.PriorityQueue(3)
        self.right_object_queue = queue.PriorityQueue(3)
        self.right_interact_queue = queue.PriorityQueue(3)
        self.left_interact_queue = queue.PriorityQueue(3)
        self.subject_instance_name = 'Mouse'
        self.left_object_name = 'LeftTeaball'
        self.right_object_name = 'RightTeaball'
        self.left_interact_name = 'LeftInteract'
        self.right_interact_name = 'RightInteract'
        self.num_instances_per_class = num_instances_per_class
        self.custom_activation = {}

        try:
            register_coco_instances(f"{dataset_name}_train", {
            }, f"{self.dataset_dir}/train/annotations.json", f"{self.dataset_dir}/train/")
            register_coco_instances(f"{dataset_name}_valid", {
            }, f"{self.dataset_dir}/valid/annotations.json", f"{self.dataset_dir}/valid/")
        except AssertionError as e:
            print(e)
        dataset_dicts = get_detection_dataset_dicts([f"{dataset_name}_train"])

        _dataset_metadata = MetadataCatalog.get(f"{dataset_name}_train")
        _dataset_metadata.thing_colors = [cc['color']
                                          for cc in builtin_meta.COCO_CATEGORIES]
        num_classes = len(_dataset_metadata.thing_classes)
        self.class_names = _dataset_metadata.thing_classes

        self.cfg = get_cfg()
        # load model config and pretrained model
        self.cfg.merge_from_file(model_zoo.get_config_file(
            model_config
        ))
        self.cfg.MODEL.WEIGHTS = model_pth_path
        self.cfg.DATASETS.TRAIN = (f"{dataset_name}_train",)
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = self.score_threshold
        self.cfg.MODEL.DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.cfg.MODEL.ROI_HEADS.NUM_CLASSES = num_classes
        self.cfg.MODEL.ROI_HEADS.NMS_THRESH_TEST = self.overlap_threshold

        # NMS threshold used on RPN proposals
        self.cfg.MODEL.RPN.NMS_THRESH = self.overlap_threshold

        self.predictor = DefaultPredictor(self.cfg)

    def to_labelme(self,
                   instances,
                   image_path,
                   height,
                   width
                   ):
        results = self._process_instances(instances, width=width)
        df_res = pd.DataFrame(results)
        df_res = df_res.groupby(['instance_name'], sort=False).head(
            self.num_instances_per_class)
        results = df_res.to_dict(orient='records')
        frame_label_list = []
        for res in results:
            label_list = pred_dict_to_labelme(res)
            frame_label_list += label_list
        img_ext = Path(image_path).suffix
        json_path = image_path.replace(img_ext, ".json")
        save_labels(json_path,
                    str(Path(image_path).name),
                    frame_label_list,
                    height,
                    width,
                    imageData=None,
                    save_image_to_json=False
                    )
        return json_path

    def on_image(self, image_path, display=True):
        """
        This function takes the path of an image file as input,
          applies instance segmentation on it,
        and displays the results if 'display' parameter is set to True.
        Args:
            image_path (str): The path of the image file.
            display (bool): Whether to display the results or not. Default is True.

        Returns:
            None
        """
        image = cv2.imread(image_path)
        height, width, _ = image.shape
        preds = self.predictor(image)
        instances = preds["instances"].to('cpu')

        # save json format for at least one predicted instance
        if len(instances) >= 1:
            self.to_labelme(instances, image_path, height, width)

        if display:
            viz = Visualizer(image[:, :, ::-1],
                             metadata=MetadataCatalog.get(
                self.cfg.DATASETS.TRAIN[0]),
                instance_mode=ColorMode.SEGMENTATION
            )
            output = viz.draw_instance_predictions(
                instances
            )
            cv2.imshow("Frame", output.get_image()[:, :, ::-1])
            cv2.waitKey(0)

    def _save_pred_history(self,
                           out_dict,
                           instance_name,
                           instance_queue
                           ):

        if out_dict['instance_name'] == instance_name:
            if instance_queue.full():
                try:
                    instance_queue.get()
                except TypeError:
                    print(
                        "Comparison between instances of 'dict' and 'dict' is not supported.")
            else:
                instance_queue.put(
                    (1-out_dict['class_score'], out_dict))

    def _overlap_with_subject_instance(self, out_dict):
        if self.subject_queue.qsize() == 0:
            return True
        subject_instance_best_score = self.subject_queue.get()
        _iou = mask_iou(
            subject_instance_best_score[1]['segmentation'],
            out_dict['segmentation']
        )
        self.subject_queue.put(subject_instance_best_score)
        if _iou <= 0:
            return False
        return True

    def _overlap_with_left_object(self,
                                  out_dict):
        if self.left_object_queue.qsize() == 0:
            return True
        left_object_best_score = self.left_object_queue.get()
        _iou = mask_iou(
            left_object_best_score[1]['segmentation'],
            out_dict['segmentation']
        )
        self.left_object_queue.put(left_object_best_score)
        return _iou > 0

    def _overlap_with_right_object(self,
                                   out_dict):
        if self.right_object_queue.qsize() == 0:
            return True
        right_object_best_score = self.right_object_queue.get()
        _iou = mask_iou(
            right_object_best_score[1]['segmentation'],
            out_dict['segmentation']
        )
        self.right_object_queue.put(right_object_best_score)
        return _iou > 0

    def subject_overlap_with_right_object(self):
        if self.right_object_queue.qsize() == 0:
            return True
        right_object_best_score = self.right_object_queue.get()
        subject_best_score = self.subject_queue.get()
        _iou = mask_iou(
            right_object_best_score[1]['segmentation'],
            subject_best_score[1]['segmentation']
        )
        self.right_object_queue.put(right_object_best_score)
        self.subject_queue.put(subject_best_score)
        return _iou > 0

    def subject_overlap_with_left_object(self):
        if self.left_object_queue.qsize() == 0:
            return True
        left_object_best_score = self.left_object_queue.get()
        subject_best_score = self.subject_queue.get()
        _iou = mask_iou(
            left_object_best_score[1]['segmentation'],
            subject_best_score[1]['segmentation']
        )
        self.left_object_queue.put(left_object_best_score)
        self.subject_queue.put(subject_best_score)
        return _iou > 0

    def _process_instances(self,
                           instances,
                           frame_number=0,
                           width=None
                           ):
        results = []
        out_dict = {}
        num_instance = len(instances)
        boxes = instances.pred_boxes.tensor
        scores = instances.scores
        classes = instances.pred_classes
        if instances.has('ID'):
            tracking_ids = instances.ID
        else:
            tracking_ids = None
        # apply nms for all the class
        _keep = nms(boxes, scores, self.overlap_threshold)
        boxes = boxes[_keep]
        scores = scores[_keep]
        classes = classes[_keep]

        boxes = boxes.numpy()
        boxes = boxes.tolist()
        scores = scores.tolist()
        classes = classes.tolist()

        has_mask = instances.has("pred_masks")

        if has_mask:
            pred_masks = instances.pred_masks
            pred_masks = pred_masks[_keep]
            rles = [
                mask_util.encode(
                    np.array(mask[:, :, None], order="F", dtype="uint8"))[0]
                for mask in pred_masks
            ]
            for rle in rles:
                rle["counts"] = rle["counts"].decode("utf-8")

        assert len(rles) == len(boxes)

        if num_instance != len(rles):
            num_instance = len(rles)
        for k in range(num_instance):
            box = boxes[k]
            out_dict['frame_number'] = frame_number
            out_dict['x1'] = box[0]
            out_dict['y1'] = box[1]
            out_dict['x2'] = box[2]
            out_dict['y2'] = box[3]
            out_dict['cx'] = (out_dict['x1'] + out_dict['x2']) / 2
            out_dict['cy'] = (out_dict['y1'] + out_dict['y2']) / 2
            out_dict['instance_name'] = self.class_names[classes[k]]
            out_dict['class_score'] = scores[k]
            out_dict['segmentation'] = rles[k]
            if len(self.class_names) <= 1:
                out_dict['tracking_id'] = 0
            else:
                out_dict['tracking_id'] = tracking_ids[k] if tracking_ids else None

            if scores[k] >= self.score_threshold:
                out_dict['instance_name'] = TracksResults.switch_left_right(
                    out_dict, width=width)

                if out_dict['instance_name'] == self.subject_instance_name:
                    self._save_pred_history(out_dict,
                                            self.subject_instance_name,
                                            self.subject_queue)

                elif out_dict['instance_name'] == self.left_object_name:
                    self._save_pred_history(out_dict,
                                            self.left_object_name,
                                            self.left_object_queue)
                elif out_dict['instance_name'] == self.right_object_name:
                    self._save_pred_history(out_dict,
                                            self.right_object_name,
                                            self.right_object_queue)
                elif out_dict['instance_name'] == self.left_interact_name:
                    self._save_pred_history(out_dict,
                                            self.left_interact_name,
                                            self.left_interact_queue)
                    # check overlap with subject animal
                    if not self._overlap_with_subject_instance(out_dict):
                        out_dict = {}
                        continue
                    # check overlap with left object

                    if not self._overlap_with_left_object(out_dict):
                        out_dict = {}
                        continue

                elif out_dict['instance_name'] == self.right_interact_name:
                    self._save_pred_history(out_dict,
                                            self.right_interact_name,
                                            self.left_interact_queue)
                    if not self._overlap_with_subject_instance(out_dict):
                        out_dict = {}
                        continue

                    if not self._overlap_with_right_object(out_dict):
                        out_dict = {}
                        continue

                results.append(out_dict)
            out_dict = {}
        return results

    def on_image_folder(self,
                        image_folder
                        ):
        """
        This function takes an image folder path as
          input and processes all the images in it.
        It finds all the .jpg or .png images in the folder
          and calls the on_image() method for each image.
        Args:
        image_folder (str): Path of the image folder

        Returns:
            None
        """
        imgs = glob.glob(str(Path(image_folder) / '*.jpg'))
        if len(imgs) <= 0:
            imgs = glob.glob(str(Path(image_folder) / '*.png'))
        for img_path in imgs:
            self.on_image(img_path, display=False)

    def on_video(self,
                 video_path,
                 skip_frames=1,
                 on_keyframes=False,
                 tracking=False
                 ):
        if not Path(video_path).exists():
            return
        self.cap = cv2.VideoCapture(video_path)
        num_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        tracker = None
        if tracking:
            from detectron2.config import CfgNode as CfgNode_
            from detectron2.tracking.base_tracker import build_tracker_head
            cfg = CfgNode_()
            cfg.TRACKER_HEADS = CfgNode_()
            cfg.TRACKER_HEADS.TRACKER_NAME = "IOUWeightedHungarianBBoxIOUTracker"
            cfg.TRACKER_HEADS.VIDEO_HEIGHT = height
            cfg.TRACKER_HEADS.VIDEO_WIDTH = width
            cfg.TRACKER_HEADS.MAX_NUM_INSTANCES = 200
            cfg.TRACKER_HEADS.MAX_LOST_FRAME_COUNT = 30
            cfg.TRACKER_HEADS.MIN_BOX_REL_DIM = 0.02
            cfg.TRACKER_HEADS.MIN_INSTANCE_PERIOD = 1
            cfg.TRACKER_HEADS.TRACK_IOU_THRESHOLD = 0.3
            tracker = build_tracker_head(cfg)

        if on_keyframes:
            out_img_dir = key_frames(video_path)
            self.on_image_folder(out_img_dir)
        tracking_results = []

        frame_number = 0
        for frame in videos.frame_from_video(self.cap, num_frames):
            if frame_number % skip_frames == 0:
                outputs = self.predictor(frame)
                out_dict = {}
                instances = outputs["instances"].to("cpu")
                if tracker:
                    instances = tracker.update(instances)
                num_instance = len(instances)
                if num_instance == 0:
                    out_dict['frame_number'] = frame_number
                    out_dict['x1'] = None
                    out_dict['y1'] = None
                    out_dict['x2'] = None
                    out_dict['y2'] = None
                    out_dict['instance_name'] = None
                    out_dict['class_score'] = None
                    out_dict['segmentation'] = None
                    out_dict['tracking_id'] = None
                    tracking_results.append(out_dict)
                    out_dict = {}
                else:
                    _res = self._process_instances(
                        instances, frame_number, width)
                    tracking_results += _res
            frame_number += 1
            if frame_number % 100 == 0:
                print("Processing frame number: ", frame_number)

            df = pd.DataFrame(tracking_results)
            df_top = df.groupby(
                ['frame_number', 'instance_name'], sort=False).head(self.num_instances_per_class)
            # tracking_results_dir = Path(self.dataset_dir).parent
            # tracking_results_csv = f"{str(Path(self.dataset_dir).stem)}"
            tracking_results_csv = f"{str(Path(video_path).with_suffix(''))}"
            tracking_results_csv += "_mask_rcnn_tracking_results_with_segmentation.csv"
            df_top.to_csv(tracking_results_csv)
        if on_keyframes:
            print(f"Done. Please check you results in folder: {out_img_dir}")
            return out_img_dir
        print(f"Done!")

    def extract_mask_roi_features(self, frame):
        """extract mask ROI features from the given video frame

        Args:
            frame (cv2.frame): video frame read by cv2

        Returns:
            numpy array: mask features
        """
        im = frame[:, :, ::-1]
        height, width = im.shape[:2]
        image = torch.as_tensor(im.astype("float32").transpose(2, 0, 1))
        inputs = [{"image": image, "height": height, "width": width}]
        images = self.predictor.model.preprocess_image(inputs)
        features = self.predictor.model.backbone(images.tensor)

        proposals, _ = self.predictor.model.proposal_generator(
            images, features)
        instances, _ = self.predictor.model.roi_heads(
            images, features, proposals)
        mask_features = [features[f]
                         for f in self.predictor.model.roi_heads.in_features]
        mask_features = self.predictor.model.roi_heads.mask_pooler(
            mask_features, [x.pred_boxes for x in instances])
        return mask_features

    def extract_backbone_features(self, frame):
        """extract backbone ROI features from the given video frame

        Args:
            frame (cv2.frame): video frame read by cv2

        Returns:
            numpy array: backbone features
        """
        im = frame[:, :, ::-1]
        height, width = im.shape[:2]
        image = torch.as_tensor(im.astype("float32").transpose(2, 0, 1))
        inputs = [{"image": image, "height": height, "width": width}]
        images = self.predictor.model.preprocess_image(inputs)

        features = self.predictor.model.backbone(images.tensor)

        return features

    def get_activation_frome_layer(self, layer_name):
        """Get output from a given layer
        e.g. usage
        self.predictor.model.
        roi_heads.box_predictor.register_forward_hook(get_activation('cls_score'))

        Args:
            layer_name (str): layer name like mask_head
        """
        def hook(model, input, output):
            self.custom_activation[layer_name] = output
        return hook
