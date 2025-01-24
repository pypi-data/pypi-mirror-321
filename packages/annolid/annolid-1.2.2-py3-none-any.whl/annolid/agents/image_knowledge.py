from pathlib import Path
from typing import Union, Iterator, List
from PIL import Image
from phi.document import Document
from phi.knowledge.agent import AgentKnowledge
from phi.utils.log import logger


class ImageReader:
    """Class to read and process image files."""

    def read(self, image_path: Path) -> Document:
        """Read an image and convert it into a Document.

        Args:
            image_path (Path): Path to the image file.

        Returns:
            Document: Document representing the image.
        """
        try:
            with Image.open(image_path) as img:
                # Copy to prevent issues with file handles.
                img_data = img.copy()
                metadata = {
                    "filename": image_path.name,
                    "size": img.size,
                    "mode": img.mode,
                }
                # Convert image data to string or handle as needed
                return Document(content=str(img_data), metadata=metadata)
        except Exception as e:
            logger.error(f"Failed to read image {image_path}: {e}")
            return Document(content="Error: Unable to process image.", metadata={"error": str(e)})


class ImageKnowledgeBase(AgentKnowledge):
    path: Union[str, Path]
    reader: ImageReader = ImageReader()

    @property
    def document_lists(self) -> Iterator[List[Document]]:
        """Iterate over image files and yield lists of Documents.

        Returns:
            Iterator[List[Document]]: Iterator yielding lists of Documents.
        """
        _image_path: Path = Path(self.path) if isinstance(
            self.path, str) else self.path

        if _image_path.exists() and _image_path.is_dir():
            for _image_file in _image_path.glob("**/*"):
                if _image_file.suffix.lower() in {".png", ".jpg", ".jpeg", ".bmp", ".tiff"}:
                    yield [self.reader.read(image_path=_image_file)]
        elif _image_path.exists() and _image_path.is_file():
            if _image_path.suffix.lower() in {".png", ".jpg", ".jpeg", ".bmp", ".tiff"}:
                yield [self.reader.read(image_path=_image_path)]
            else:
                logger.error(f"Unsupported image format: {_image_path}")
        else:
            logger.error(f"Invalid path: {_image_path}")
