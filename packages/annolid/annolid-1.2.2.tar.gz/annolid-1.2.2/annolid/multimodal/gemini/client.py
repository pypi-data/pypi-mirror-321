import logging
from google import genai
from config import GeminiConfig

# Set up logging for better traceability
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GeminiClient:
    def __init__(self, api_key=None):
        """
        Initializes the Gemini client with the provided API key or defaults to the environment variable.
        """
        self.api_key = api_key or GeminiConfig.API_KEY
        if not self.api_key:
            raise ValueError("API Key is required for Gemini Client.")
        self.client = genai.Client(api_key=self.api_key)
        logger.info("Gemini client initialized with API key.")

    def generate_content(self, contents: str, model_id: str = None, response_modalities: list = None):
        """
        Generates content using the Gemini API with the given input.

        Args:
            contents (str): The text prompt for content generation.
            model_id (str): The ID of the model to use (defaults to GeminiConfig).
            response_modalities (list): The modalities for the response (defaults to GeminiConfig).

        Returns:
            dict: The generated content response.
        """
        model_id = model_id or GeminiConfig.MODEL_ID
        response_modalities = response_modalities or GeminiConfig.RESPONSE_MODALITIES

        try:
            logger.info(
                f"Generating content with model {model_id} for prompt: {contents[:50]}...")

            response = self.client.models.generate_content(
                model=model_id,
                contents=contents,
                config={"response_modalities": response_modalities}
            )

            logger.info("Content generated successfully.")
            return response
        except Exception as e:
            logger.error(f"Error generating content: {e}")
            raise
