import whisper

# Load once (important for performance)
model = whisper.load_model("small")

def transcribe(audio_path):
    result = model.transcribe(
        audio_path,
        word_timestamps=False
    )
    return result["segments"], result["language"]
