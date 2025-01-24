from client import GeminiClient


def query_gemini_for_text(query: str, model_id: str = None):
    """
    Function to query the Gemini API for text generation.

    Args:
        query (str): The input text prompt.
        model_id (str): Model ID to use.

    Returns:
        str: Generated content from Gemini.
    """
    client = GeminiClient()  # Initialize the Gemini Client
    response = client.generate_content(contents=query, model_id=model_id)
    return response.text if response and hasattr(response, "text") else "No response generated."


def handle_gemini_response(response):
    """
    Handle the response from Gemini API (e.g., logging, processing).

    Args:
        response: The response object returned by the Gemini API.

    Returns:
        str: Processed content.
    """
    if response and hasattr(response, "text"):
        # You can process further here (e.g., logging or transformation)
        return response.text
    else:
        raise ValueError("Invalid response from Gemini API.")
