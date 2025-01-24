from typing import List, Tuple, Optional, Dict, Any
import torch
import clip
from PIL import Image
from phi.embedder.base import Embedder
from phi.utils.log import logger


class CLIPEmbedder(Embedder):
    model_name: str = "ViT-B/32"  # Default model
    dimensions: int = 512  # CLIP ViT-B/32 output dimensions
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    model: Optional[torch.nn.Module] = None
    preprocess: Optional[Any] = None

    def __post_init__(self):
        # Load the CLIP model and preprocessing pipeline
        try:
            self.model, self.preprocess = clip.load(
                self.model_name, device=self.device)
        except Exception as e:
            logger.error(f"Failed to load CLIP model: {e}")
            raise RuntimeError("CLIP model initialization failed")

    def get_text_embedding(self, text: str) -> List[float]:
        """Compute text embedding using CLIP."""
        try:
            tokens = clip.tokenize([text]).to(self.device)
            with torch.no_grad():
                text_features = self.model.encode_text(tokens)
            return text_features.cpu().numpy().flatten().tolist()
        except Exception as e:
            logger.warning(f"Error generating text embedding: {e}")
            return []

    def get_embedding(self, image_path: str) -> List[float]:
        """Compute image embedding using CLIP."""
        try:
            image = Image.open(image_path).convert("RGB")
            image_input = self.preprocess(image).unsqueeze(0).to(self.device)
            with torch.no_grad():
                image_features = self.model.encode_image(image_input)
            return image_features.cpu().numpy().flatten().tolist()
        except Exception as e:
            logger.warning(f"Error generating image embedding: {e}")
            return []
        

    def get_embedding_and_usage(self, text: Optional[str] = None, image_path: Optional[str] = None) -> Tuple[List[float], Optional[Dict]]:
        """Compute embedding for text or image and return usage info (dummy implementation)."""
        embedding = []
        usage = None  # Placeholder for additional metadata
        try:
            if text:
                embedding = self.get_text_embedding(text)
            elif image_path:
                embedding = self.get_image_embedding(image_path)
            else:
                logger.warning("Either text or image_path must be provided.")
        except Exception as e:
            logger.warning(e)
        return embedding, usage
