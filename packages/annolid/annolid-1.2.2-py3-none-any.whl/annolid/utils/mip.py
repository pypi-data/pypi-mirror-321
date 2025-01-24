import json
import cv2
import numpy as np
from shapely.geometry import Polygon
from PIL import Image
from labelme.utils.shape import shapes_to_label
import os


def load_shapes_from_json(json_file, image_size):
    """
    Load shapes from a JSON file and convert them to a binary mask.

    Args:
        json_file (str): Path to the label JSON file.
        image_size (tuple): Size of the image (height, width).

    Returns:
        mask: Binary mask where different objects have unique IDs.
        label_name_to_value: A dictionary mapping labels to their corresponding values in the mask.
    """
    label_name_to_value = {"_background_": 0}
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    shapes = [shape for shape in data.get('shapes', []) if len(shape["points"]) >= 3]
    
    for shape in sorted(shapes, key=lambda x: x["label"]):
        label_name = shape["label"]
        if label_name not in label_name_to_value:
            label_value = len(label_name_to_value)
            label_name_to_value[label_name] = label_value

    mask, _ = shapes_to_label(image_size, shapes, label_name_to_value)
    return mask, label_name_to_value

def overlay_mask_on_frame(frame, mask):
    """
    Overlay the mask onto the frame.

    Args:
        frame (ndarray): The original frame.
        mask (ndarray): The binary mask with object IDs.
    
    Returns:
        visualization: The frame with the mask overlay.
    """
    # Assign unique colors to each object ID
    mask_colored = color_id_mask(mask)

    # Overlay the colored mask onto the original frame
    overlay = cv2.addWeighted(frame, 0.7, mask_colored, 0.3, 0)
    
    return overlay

def color_id_mask(mask):
    """
    Convert object IDs in the mask to unique colors.

    Args:
        mask (ndarray): The binary mask with object IDs.

    Returns:
        color_mask (ndarray): The mask where each object ID is colored uniquely.
    """
    color_mask = np.zeros((mask.shape[0], mask.shape[1], 3), dtype=np.uint8)
    unique_ids = np.unique(mask)

    for obj_id in unique_ids:
        if obj_id == 0:
            continue  # Skip the background
        color = tuple(np.random.randint(0, 255, 3).tolist())  # Random color
        color_mask[mask == obj_id] = color

    return color_mask


def process_video_with_mask_overlay(video_path, start_frame=0,end_frame=100):
    """
    Process video and overlay the mask from JSON file for each frame.

    Args:
        video_name (str): Path to the video file.
    """
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
            

    frame_height, frame_width = frame.shape[:2]
    # frame_number = start_frame

    # Set the frame position
    #
    for frame_number in range(start_frame, end_frame):
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        json_file =  os.path.join(f"{os.path.splitext(video_path)[0]}",f"{video_name}_{frame_number:09d}.json")
        if os.path.exists(json_file):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            ret, frame = cap.read()
            
            if not ret:
                break
            # Load the shapes from the JSON and convert them to a mask
            mask, label_dict = load_shapes_from_json(json_file, (frame_height, frame_width))
            # Overlay the mask onto the current frame
            overlay_frame = overlay_mask_on_frame(frame, mask)
    return overlay_frame



 

if __name__ == '__main__':
    overlay_frame = process_video_with_mask_overlay("/Users/chenyang/Downloads/mouse.mp4",0,42)
    cv2.imwrite("over_lay.png",overlay_frame)