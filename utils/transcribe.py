from faster_whisper import WhisperModel

# CPU-only, Streamlit-safe
model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

def transcribe(file_path):
    segments_gen, info = model.transcribe(
        file_path,
        beam_size=5
    )

    segments = []
    for seg in segments_gen:
        segments.append({
            "start": seg.start,
            "end": seg.end,
            "text": seg.text
        })

    return segments, info.language
