import os
import json
import logging
from urllib.parse import urlparse
from dataclasses import dataclass
from typing import List, Union, Optional, Dict, Any
import requests
from PIL import Image, ImageDraw, ImageColor
from google import genai
from google.genai import types
from config import GeminiConfig


class ImageProcessingError(Exception):
    """Custom exception for image processing errors."""
    pass


@dataclass
class BoundingBox:
    """
    Dataclass representing a bounding box annotation.

    Attributes:
        label (str): Label for the detected object
        coordinates (List[float]): Normalized coordinates [y1, x1, y2, x2]
    """
    label: str
    coordinates: List[float]

    def to_absolute(self, image_width: int, image_height: int) -> Dict[str, int]:
        """
        Convert normalized coordinates to absolute pixel coordinates.

        Args:
            image_width (int): Width of the image
            image_height (int): Height of the image

        Returns:
            Dict[str, int]: Absolute pixel coordinates
        """
        abs_y1 = int(self.coordinates[0] / 1000 * image_height)
        abs_x1 = int(self.coordinates[1] / 1000 * image_width)
        abs_y2 = int(self.coordinates[2] / 1000 * image_height)
        abs_x2 = int(self.coordinates[3] / 1000 * image_width)

        return {
            'x1': min(abs_x1, abs_x2),
            'y1': min(abs_y1, abs_y2),
            'x2': max(abs_x1, abs_x2),
            'y2': max(abs_y1, abs_y2)
        }


class ImageAnnotator:
    """
    Handles image annotation and visualization.
    """

    def __init__(self, color_palette: Optional[List[str]] = None):
        """
        Initialize the ImageAnnotator.

        Args:
            color_palette (Optional[List[str]]): Custom color palette for annotations
        """
        self.logger = logging.getLogger(self.__class__.__name__)

        # Combine predefined colors with PIL colormap
        default_colors = [
            'red', 'green', 'blue', 'yellow', 'orange', 'pink', 'purple',
            'brown', 'gray', 'beige', 'turquoise', 'cyan', 'magenta',
            'lime', 'navy', 'maroon', 'teal', 'olive', 'coral',
            'lavender', 'violet', 'gold', 'silver'
        ]
        additional_colors = [
            colorname for colorname, _ in ImageColor.colormap.items()
            if colorname not in default_colors
        ]

        self.colors = color_palette or (default_colors + additional_colors)

    def annotate_image(
        self,
        image: Image.Image,
        bounding_boxes: List[BoundingBox]
    ) -> Dict[str, Any]:
        """
        Annotate an image with bounding boxes.

        Args:
            image (Image.Image): Input image
            bounding_boxes (List[BoundingBox]): List of bounding boxes to draw

        Returns:
            Dict[str, Any]: Annotation metadata
        """
        draw = ImageDraw.Draw(image)
        width, height = image.size
        annotations = []

        for i, bbox in enumerate(bounding_boxes):
            color = self.colors[i % len(self.colors)]
            abs_coords = bbox.to_absolute(width, height)

            # Draw bounding box
            draw.rectangle(
                ((abs_coords['x1'], abs_coords['y1']),
                 (abs_coords['x2'], abs_coords['y2'])),
                outline=color,
                width=4
            )

            # Draw label
            draw.text(
                (abs_coords['x1'] + 8, abs_coords['y1'] + 6),
                bbox.label,
                fill=color
            )

            # Collect annotations
            annotations.append({
                'label': bbox.label,
                'bbox': [
                    abs_coords['x1'], abs_coords['y1'],
                    abs_coords['x2'], abs_coords['y2']
                ]
            })

        return {
            'annotated_image': image,
            'annotations': annotations
        }

    def save_annotations(self, annotations: List[Dict[str, Any]], filepath: str):
        """
        Save annotations to a JSON file.

        Args:
            annotations (List[Dict[str, Any]]): List of annotation dictionaries
            filepath (str): Path to save the JSON file
        """
        try:
            with open(filepath, 'w') as f:
                json.dump({'annotations': annotations}, f, indent=4)
            self.logger.info(f"Annotations saved to {filepath}")
        except IOError as e:
            self.logger.error(f"Failed to save annotations: {e}")
            raise ImageProcessingError(
                f"Could not save annotations to {filepath}")


class GeminiImageProcessor:
    """
    Image processing class using Google's Gemini API for object detection.
    """

    def __init__(
        self,
        api_key: str,
        model_name: str = "gemini-2.0-flash-exp",
        temperature: float = 0.5
    ):
        """
        Initialize Gemini Image Processor.

        Args:
            api_key (str): Google Gemini API key
            model_name (str): Gemini model to use
            temperature (float): Sampling temperature for generation
        """
        self.logger = logging.getLogger(self.__class__.__name__)

        # Configure Gemini client
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name
        self.temperature = temperature

        # Safety and system instructions
        self.safety_settings = [
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="BLOCK_ONLY_HIGH",
            ),
        ]
        self.system_instructions = (
            "Return bounding boxes as a JSON array with labels. "
            "Never return masks or code fencing. Limit to 25 objects. "
            "If an object is present multiple times, name them according to "
            "their unique characteristic (colors, size, position, etc.)."
        )

        # Image annotator
        self.annotator = ImageAnnotator()

    def _load_image(self, image: Union[str, Image.Image]) -> Image.Image:
        """
        Load image from URL, local file path, or PIL Image.

        Args:
            image (Union[str, Image.Image]): Image source

        Returns:
            Image.Image: Loaded and processed image

        Raises:
            ImageProcessingError: If image cannot be loaded
        """
        try:
            if isinstance(image, str):
                # Check if the string is a URL
                parsed_url = urlparse(image)
                if parsed_url.scheme in ('http', 'https'):
                    # Load from URL
                    response = requests.get(image, stream=True)
                    response.raise_for_status()
                    image = Image.open(response.raw)
                elif os.path.isfile(image):
                    # Load from local file path
                    image = Image.open(image)
                else:
                    raise FileNotFoundError(f"No such file: {image}")

            if not isinstance(image, Image.Image):
                raise TypeError("Invalid image type")

            return image
        except (requests.RequestException, IOError, FileNotFoundError) as e:
            self.logger.error(f"Image loading failed: {e}")
            raise ImageProcessingError(f"Could not load image: {e}")

    def _parse_bounding_boxes(self, bounding_box_json: str) -> List[BoundingBox]:
        """
        Parse bounding box JSON to BoundingBox objects.

        Args:
            bounding_box_json (str): JSON string of bounding boxes

        Returns:
            List[BoundingBox]: Parsed bounding boxes
        """
        try:
            # Remove markdown fencing if present
            if '```json' in bounding_box_json:
                bounding_box_json = bounding_box_json.split('```json')[
                    1].split('```')[0]

            bbox_data = json.loads(bounding_box_json)
            return [
                BoundingBox(
                    label=box.get('label', 'unknown'),
                    coordinates=box['box_2d']
                ) for box in bbox_data
            ]
        except (json.JSONDecodeError, KeyError) as e:
            self.logger.error(f"Bounding box parsing failed: {e}")
            raise ImageProcessingError(f"Invalid bounding box format: {e}")

    def generate_bounding_boxes(
        self,
        image: Union[str, Image.Image],
        prompt: str
    ) -> Dict[str, Any]:
        """
        Generate and annotate bounding boxes for an image.

        Args:
            image (Union[str, Image.Image]): Image to process
            prompt (str): Prompt for object detection

        Returns:
            Dict[str, Any]: Processed image and annotations
        """
        try:
            # Load and resize image
            img = self._load_image(image)
            img_resized = img.resize(
                (1024, int(1024 * img.size[1] / img.size[0])),
                Image.Resampling.LANCZOS
            )

            # Generate bounding boxes using Gemini
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=[prompt, img_resized],
                config=types.GenerateContentConfig(
                    system_instruction=self.system_instructions,
                    temperature=self.temperature,
                    safety_settings=self.safety_settings,
                ),
            )

            # Parse and annotate bounding boxes
            bounding_boxes = self._parse_bounding_boxes(response.text)
            annotation_result = self.annotator.annotate_image(
                img, bounding_boxes)

            # Save annotations
            self.annotator.save_annotations(
                annotation_result['annotations'],
                'bounding_boxes_annolid.json'
            )

            return annotation_result

        except Exception as e:
            self.logger.error(f"Bounding box generation failed: {e}")
            raise ImageProcessingError(
                f"Could not generate bounding boxes: {e}")


def main():
    """
    Example usage and demonstration.
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    try:
        # Replace with your actual API key
        # Initialize the processor with your API key
        processor = GeminiImageProcessor(GeminiConfig.API_KEY)

        # Or a local file path or a PIL Image object
        _image_url = "CaMKII 2-8 N CNO ONLY 3-9-23-Trial 3_frame15090.png"
        prompt = "mouse with wire and not"

        result = processor.generate_bounding_boxes(_image_url, prompt)
        result['annotated_image'].show()

    except ImageProcessingError as e:
        logging.error(f"Image processing failed: {e}")


if __name__ == "__main__":
    main()
