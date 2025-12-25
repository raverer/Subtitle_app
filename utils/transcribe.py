import whisper

# Load model once (important for performance)
model = whisper.load_model("small")

def transcribe(file_path):
    """
    Transcribes audio or video and returns:
    - segments (with timestamps)
    - detected language
    """
    result = model.transcribe(file_path)
    return result["segments"], result["language"]
