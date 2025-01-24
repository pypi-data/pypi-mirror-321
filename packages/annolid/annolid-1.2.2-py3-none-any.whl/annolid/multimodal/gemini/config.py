import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Configuration class for loading Gemini API key and model settings
class GeminiConfig:
    API_KEY = os.getenv("Gemini_API_KEY")
    MODEL_ID = "gemini-2.0-flash-exp"  # Default model for your use case
    RESPONSE_MODALITIES = ["TEXT"]