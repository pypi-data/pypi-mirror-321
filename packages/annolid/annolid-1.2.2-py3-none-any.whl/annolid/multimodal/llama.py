import cv2
import json
import ollama

def analyze_image_with_ollama(image_bytes: bytes, object_str: str):
    """Analyzes an image from bytes using the Ollama model."""
    prompt_str = f"""Please analyze the image and answer the following questions:
    1. Is there a {object_str} in the image?
    2. If yes, describe its appearance and location in the image in detail.
    3. If no, describe what you see in the image instead.
    4. On a scale of 1-10, how confident are you in your answer?

    Please structure your response as follows:
    Answer: [YES/NO]
    Description: [Your detailed description]
    Confidence: [1-10]"""

    try:
        response = ollama.chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': prompt_str,
                'images': [image_bytes]
            }]
        )

        response_text = response['message']['content']
        response_lines = response_text.strip().split('\n')

        answer = None
        description = None
        confidence = 10

        for line in response_lines:
            line = line.strip()
            if line.lower().startswith('answer:'):
                answer = line.split(':', 1)[1].strip().upper()
            elif any(line.lower().startswith(prefix) for prefix in
                     ['description:', 'reasoning:', 'alternative description:']):
                description = line.split(':', 1)[1].strip()
            elif line.lower().startswith('confidence:'):
                try:
                    confidence = int(line.split(':', 1)[1].strip())
                except ValueError:
                    confidence = 10

        return answer == "YES" and confidence >= 7, description, confidence
    except Exception as e:
        print(f"Error during image analysis: {str(e)}")
        return False, "Error occurred", 0


def analyze_video(video_path: str, object_str: str):
    """Processes a video and analyzes frames for the specified object."""
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = 0

    results = []

    try:
        while True:
            success, frame = cap.read()
            if not success:
                break

            if frame_count % fps == 0:  # Process one frame per second
                current_second = frame_count // fps

                # Encode frame to bytes
                _, frame_bytes = cv2.imencode('.jpg', frame)
                frame_bytes = frame_bytes.tobytes()

                # Preprocess and analyze the frame directly using bytes
                is_match, description, confidence = analyze_image_with_ollama(
                    frame_bytes, object_str
                )

                result = {
                    "second": current_second,
                    "is_match": is_match,
                    "description": description,
                    "confidence": confidence
                }
                results.append(result)

            frame_count += 1

    finally:
        cap.release()

    return results


# Example usage
if __name__ == "__main__":
    video_file_path = "/Users/chenyang/Downloads/mouse.mp4"
    # Replace with the object you are interested in
    object_to_detect = "a black mouse"

    analysis_results = analyze_video(video_file_path, object_to_detect)
    for result in analysis_results:
        print(json.dumps(result, indent=2))
