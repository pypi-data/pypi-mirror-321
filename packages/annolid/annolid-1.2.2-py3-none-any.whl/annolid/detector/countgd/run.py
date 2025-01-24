import random
import torch
from PIL import Image
import numpy as np
import argparse
import json
import os
from util.slconfig import SLConfig
from util.misc import nested_tensor_from_tensor_list
import datasets.transforms as T
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt
import io
import warnings
from annolid.utils.devices import get_device
from annolid.gui.shape import Shape

warnings.filterwarnings("ignore")

DEFAULT_CONF_THRESH = 0.23


def build_transforms(size: int = 800, max_size: int = 1333) -> T.Compose:
    """Builds data transformations for image preprocessing.

    Args:
        size: The size to which the shorter side of the image will be resized.
        max_size: Maximum size of the longer side of the image after resizing.

    Returns:
        A composition of data transformations.
    """
    normalize = T.Compose(
        [T.ToTensor(), T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]
    )
    return T.Compose([T.RandomResize([size], max_size=max_size), normalize])


def load_model(
    model_path: str, config_path: str = "cfg_app.py", device: str = get_device()
) -> torch.nn.Module:
    """Loads the counting model from a checkpoint.

    Args:
        model_path: Path to the pretrained model checkpoint.
        config_path: Path to the configuration file.
        device: Device to load the model onto.

    Returns:
        The loaded counting model.
    """
    cfg = SLConfig.fromfile(config_path)
    cfg.merge_from_dict({"text_encoder_type": "checkpoints/bert-base-uncased"})

    parser = argparse.ArgumentParser("Model Config")
    args = parser.parse_args()

    cfg_dict = cfg._cfg_dict.to_dict()
    args_vars = vars(args)
    for k, v in cfg_dict.items():
        if k not in args_vars:
            setattr(args, k, v)
        elif args_vars[k] != v:  # Allow overriding config with command-line args
            print(
                f"Warning: Overriding config parameter '{k}' with command-line value.")

    seed = 42
    torch.manual_seed(seed)
    np.random.seed(seed)
    random.seed(seed)

    from models.registry import MODULE_BUILD_FUNCS

    if args.modelname not in MODULE_BUILD_FUNCS._module_dict:
        raise ValueError(
            f"Model name '{args.modelname}' not found in registry.")
    build_func = MODULE_BUILD_FUNCS.get(args.modelname)
    model, _, _ = build_func(args)

    checkpoint = torch.load(model_path, map_location="cpu")["model"]
    model.load_state_dict(checkpoint, strict=False)
    model.to(device).eval()
    return model


def _get_box_inputs(prompts: list) -> list:
    """Extracts bounding box coordinates from prompt data.

    Args:
        prompts: A list of prompt data.

    Returns:
        A list of bounding box coordinates.
    """
    return [
        [prompt[0], prompt[1], prompt[3], prompt[4]]
        for prompt in prompts
        if prompt[2] == 2.0 and prompt[5] == 3.0
    ]


def _get_ind_to_filter(text: str, word_ids: list, keywords: str) -> list:
    """Determines the indices of word IDs to filter based on keywords.

    Args:
        text: The input text prompt.
        word_ids: List of word IDs from the model output.
        keywords: Comma-separated keywords to filter.

    Returns:
        A list of indices to filter.
    """
    if not keywords:
        return list(range(len(word_ids)))

    input_words = text.split()
    keywords_list = [keyword.strip() for keyword in keywords.split(",")]

    word_inds = []
    for keyword in keywords_list:
        try:
            start_index = 0 if not word_inds else word_inds[-1] + 1
            ind = input_words.index(keyword, start_index)
            word_inds.append(ind)
        except ValueError:
            raise ValueError(
                f"Keyword '{keyword}' not found in input text: '{text}'")

    inds_to_filter = [ind for ind, word_id in enumerate(
        word_ids) if word_id in word_inds]
    return inds_to_filter


def visualize_results(image: Image.Image, boxes: np.ndarray) -> Image.Image:
    """Visualizes detection results on the input image.

    Args:
        image: The input image.
        boxes: Array of bounding boxes in normalized coordinates.

    Returns:
        The image with overlaid detection heatmap.
    """
    w, h = image.size
    det_map = np.zeros((h, w))
    if len(boxes) > 0:
        y_coords = (h * boxes[:, 1]).astype(int)
        x_coords = (w * boxes[:, 0]).astype(int)
        det_map[y_coords, x_coords] = 1
    det_map = ndimage.gaussian_filter(
        det_map, sigma=(w // 200, w // 200), order=0)

    plt.imshow(image)
    plt.imshow(det_map, "jet", interpolation="none", alpha=0.7)
    plt.axis("off")
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format="png", bbox_inches="tight")
    plt.close()
    return Image.open(img_buf)


def count_objects(
    image_path: str,
    text_prompt: str,
    exemplar_image_path: str = None,
    exemplar_boxes: list = None,
    model: torch.nn.Module = None,
    transform: T.Compose = None,
    device: str = get_device(),
    config_path: str = "cfg_app.py",
    confidence_threshold: float = DEFAULT_CONF_THRESH,
    keywords: str = "",
) -> tuple[Image.Image, int, np.ndarray]:
    """Counts objects in an image based on a text prompt and optional visual exemplars.

    Args:
        image_path: Path to the input image.
        text_prompt: Textual description of the object to count.
        exemplar_image_path: Path to the exemplar image (optional).
        exemplar_boxes: List of exemplar bounding boxes in normalized [xmin, ymin, xmax, ymax] format (optional).
        model: Pre-loaded counting model (optional).
        transform: Pre-built data transformation pipeline (optional).
        device: Device to run inference on (optional).
        config_path: Path to the model configuration file (optional).
        confidence_threshold: Confidence threshold for object detection (optional).
        keywords: Comma-separated keywords to filter detected objects (optional).

    Returns:
        A tuple containing the output image with detections, the predicted count, and the detected bounding boxes (normalized).
    """
    if model is None or transform is None:
        raise ValueError(
            "Both 'model' and 'transform' must be provided if not pre-loaded."
        )

    image = Image.open(image_path).convert("RGB")
    exemplar_prompts = {"image": None, "points": []}

    if exemplar_image_path:
        exemplar_prompts["image"] = Image.open(
            exemplar_image_path).convert("RGB")
        if exemplar_boxes:
            exemplar_prompts["points"] = [
                [box[0], box[1], 2.0, box[2], box[3], 3.0] for box in exemplar_boxes
            ]

    input_image, _ = transform(image, {"exemplars": torch.tensor([])})
    input_image = input_image.unsqueeze(0).to(device)
    exemplars_boxes_tensor = _get_box_inputs(
        exemplar_prompts.get("points", []))

    input_image_exemplars = None
    exemplars_tensor = []
    if exemplar_prompts.get("image") is not None:
        exemplar_image = exemplar_prompts["image"]
        input_image_exemplars, exemplars_transformed = transform(
            exemplar_image, {"exemplars": torch.tensor(exemplars_boxes_tensor)}
        )
        input_image_exemplars = input_image_exemplars.unsqueeze(0).to(device)
        exemplars_tensor = [exemplars_transformed["exemplars"].to(device)]

    with torch.no_grad():
        model_output = model(
            nested_tensor_from_tensor_list(input_image),
            nested_tensor_from_tensor_list(
                input_image_exemplars) if input_image_exemplars is not None else None,
            exemplars_tensor,
            [torch.tensor([0]).to(device)] * len(input_image),
            captions=[text_prompt + " ."] * len(input_image),
        )

    ind_to_filter = _get_ind_to_filter(
        text_prompt, model_output["token"][0].word_ids, keywords
    )
    logits = model_output["pred_logits"].sigmoid()[0][:, ind_to_filter]
    boxes = model_output["pred_boxes"][0]

    if keywords.strip():
        box_mask = (logits > confidence_threshold).sum(
            dim=-1) == len(ind_to_filter)
    else:
        box_mask = logits.max(dim=-1).values > confidence_threshold

    filtered_logits = logits[box_mask, :].cpu().numpy()
    filtered_boxes = boxes[box_mask, :].cpu().numpy()

    output_img = visualize_results(image, filtered_boxes)

    return output_img, filtered_boxes.shape[0], filtered_boxes


def get_shapes(image: Image.Image, boxes: np.ndarray, label: str) -> list:
    """Converts detected bounding boxes to Labelme rectangle shape format.

    Args:
        image: The original input image.
        boxes: Array of bounding boxes in normalized coordinates (center_x, center_y, width, height).
        label: The label to assign to the shapes.

    Returns:
        A list of dictionaries, each representing a Labelme rectangle shape.
    """
    h, w = image.height, image.width
    shapes = []
    for box in boxes:
        center_x, center_y, box_w, box_h = box
        x1 = int((center_x - box_w / 2) * w)
        y1 = int((center_y - box_h / 2) * h)
        x2 = int((center_x + box_w / 2) * w)
        y2 = int((center_y + box_h / 2) * h)
        # shape = {
        #     "label": label,
        #     "points": [[x1, y1], [x2, y2]],
        #     "shape_type": "rectangle",
        #     "group_id": None,
        #     "flags": {},
        # }
        shape = {
            "label": label,
            "points": [[int(center_x*w), int(center_y*h)]],
            "shape_type": "point",
            "group_id": None,
            "flags": {},
        }
        shapes.append(shape)
    return shapes


def save_labelme_json(image_path: str, shapes: list, output_path: str = None) -> None:
    """Saves the detected bounding boxes in Labelme JSON format.

    Args:
        image_path: Path to the original image.
        shapes: List of Labelme shape dictionaries.
        output_path: Path to save the JSON file. Defaults to replacing the image extension with .json.
    """
    if output_path is None:
        output_path = os.path.splitext(image_path)[0] + ".json"

    _, filename = os.path.split(image_path)
    image_pil = Image.open(image_path)
    imageData = None  # Can be base64 encoded image data if needed

    json_data = {
        "version": "5.2.1",  # Example version
        "flags": {},
        "shapes": shapes,
        "imagePath": filename,
        "imageData": imageData,
        "imageHeight": image_pil.height,
        "imageWidth": image_pil.width,
    }

    with open(output_path, "w") as f:
        json.dump(json_data, f, indent=4)
    print(f"Labelme JSON saved to {output_path}")


if __name__ == "__main__":
    input_image_path = "strawberry.jpg"  # Replace with your image path
    text_prompt = "blueberries"
    # Replace with your exemplar image path, or None
    exemplar_image_path = "strawberry.jpg"
    exemplar_boxes = [[0.1, 0.1, 0.2, 0.2]]  # Example box

    pretrain_model_path = "checkpoint_best_regular.pth"  # Replace with your model path
    config_path = "cfg_app.py"  # Replace with your config path if different

    # Load model and transforms once
    model = load_model(pretrain_model_path, config_path=config_path)
    transform = build_transforms()

    output_image, predicted_count, detected_boxes = count_objects(
        input_image_path,
        text_prompt,
        exemplar_image_path=exemplar_image_path,
        exemplar_boxes=exemplar_boxes,
        confidence_threshold=0.3,
        keywords="blueberries",
        model=model,
        transform=transform,
    )
    print(f"Predicted count: {predicted_count}")
    output_image.show()

    # Get shapes for Labelme
    image = Image.open(input_image_path).convert("RGB")
    labelme_shapes = get_shapes(image, detected_boxes, text_prompt)
    print("Labelme Shapes:")
    for shape in labelme_shapes:
        print(shape)

    # Save to Labelme JSON
    save_labelme_json(input_image_path, labelme_shapes)
