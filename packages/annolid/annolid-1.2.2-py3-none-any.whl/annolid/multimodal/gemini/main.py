from utils import query_gemini_for_text
from spatial_2d import GeminiImageProcessor
from PIL import Image
from config import GeminiConfig

def main():
    # prompt = "How does AI work?"
    # print("Querying Gemini 2.0 for:", prompt)

    # try:
    #     response = query_gemini_for_text(prompt)
    #     print("Generated Content:", response)
    # except Exception as e:
    #     print("Error during content generation:", str(e))

    # Initialize the processor with your API key
    processor = GeminiImageProcessor(GeminiConfig.API_KEY)

    # Or a local file path or a PIL Image object
    _image_url = Image.open("CaMKII 1-8 M R 2-8-21-Phase 3_frame3772.png")
    prompt = "mouse with wire and not"

    processor.generate_bounding_boxes(_image_url, prompt)

if __name__ == "__main__":
    main()