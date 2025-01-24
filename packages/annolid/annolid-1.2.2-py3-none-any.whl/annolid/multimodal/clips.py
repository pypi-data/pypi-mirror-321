from eva_clip import build_eva_model_and_transforms
import os
import sys
import argparse
from glob import glob
from typing import List, Generator, Optional
import torch
from tqdm import tqdm
from PIL import Image
import logging
import cv2


# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Add path for custom module
sys.path.append("./EVA_clip")


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Extract and save video frame features using a CLIP model.")
    parser.add_argument("--device", type=int, default=0, help="GPU device ID")
    parser.add_argument("--slice_start", type=int, default=0,
                        help="Start index for video processing")
    parser.add_argument("--slice_end", type=int, default=-1,
                        help="End index for video processing")
    parser.add_argument("--frame_path", type=str,
                        required=True, help="Path to video frames")
    parser.add_argument("--save_path", type=str,
                        required=True, help="Path to save features")
    parser.add_argument("--batch_size", type=int, default=256,
                        help="Batch size for processing")
    return parser.parse_args()


def initialize_model(device: str, weights_path: str) -> tuple:
    """Initializes the EVA-CLIP model and preprocessing function."""
    try:
        model, preprocess = build_eva_model_and_transforms(
            "EVA_CLIP_g_14", pretrained=weights_path)
        model = model.to(device)
        model.eval()  # Set model to evaluation mode
        logging.info("Model loaded and set to evaluation mode.")
        return model, preprocess
    except Exception as e:
        logging.error(f"Failed to load the model: {e}")
        sys.exit(1)


def divide_chunks(lst: List[torch.Tensor], chunk_size: int) -> Generator[List[torch.Tensor], None, None]:
    """Splits a list into chunks."""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]


def process_video_frames(video_path: str, preprocess,
                         device: str, batch_size: int,
                         model) -> Optional[torch.Tensor]:
    """Processes and extracts features from video frames using OpenCV."""
    try:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            logging.warning(f"Failed to open video: {video_path}")
            return None

        images = []
        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert frame from BGR (OpenCV default) to RGB (PIL and most ML models use RGB)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)
            processed_image = preprocess(pil_image).cpu()
            images.append(processed_image)
            frame_count += 1

        cap.release()  # Release the video capture resource

        if not images:
            logging.warning(f"No frames extracted from {video_path}")
            return None

        images_tensor = torch.stack(images)
        feature_batches = []

        for chunk in divide_chunks(images_tensor, batch_size):
            with torch.no_grad():
                features = model.encode_image(chunk.to(device)).cpu()
                feature_batches.append(features)

        video_features = torch.cat(feature_batches)
        video_features /= video_features.norm(dim=-1, keepdim=True)
        logging.info(f"Processed {frame_count} frames from {video_path}")

        return video_features
    except Exception as e:
        logging.error(f"Error processing video {video_path}: {e}")
        return None


def save_features(features: torch.Tensor, save_path: str, video_name: str) -> None:
    """Saves the extracted features as a .pt file."""
    try:
        if features is not None:
            os.makedirs(save_path, exist_ok=True)
            torch.save(features, os.path.join(save_path, f"{video_name}.pt"))
            logging.info(f"Features saved for {video_name}")
        else:
            logging.warning(
                f"Features not saved for {video_name} due to an issue.")
    except Exception as e:
        logging.error(f"Failed to save features for {video_name}: {e}")


def main():
    """Main function to orchestrate the feature extraction."""
    args = parse_arguments()
    device = f"cuda:{args.device}" if torch.cuda.is_available() else "cpu"
    model, preprocess = initialize_model(
        device, "./pretrained_weights/eva_clip_psz14.pt")

    # Get list of videos to process
    video_paths = glob(f"{args.frame_path}/*/")
    if args.slice_end != -1:
        video_paths = video_paths[args.slice_start:args.slice_end]
    else:
        video_paths = video_paths[args.slice_start:]

    for video_path in tqdm(video_paths, colour="green"):
        video_name = os.path.basename(os.path.dirname(video_path))
        features = process_video_frames(
            video_path, preprocess, device, args.batch_size, model)
        save_features(features, args.save_path, video_name)


if __name__ == "__main__":
    main()
