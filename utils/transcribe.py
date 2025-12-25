from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="float32"   # IMPORTANT: accuracy > speed
)

def transcribe(file_path):
    segments_gen, info = model.transcribe(
        file_path,
        language="hi",        # Force Hindi (works well for Hinglish)
        beam_size=10,         # Better decoding
        vad_filter=True       # Removes noise / silence
    )

    segments = []
    for seg in segments_gen:
        segments.append({
            "start": seg.start,
            "end": seg.end,
            "text": seg.text.strip()
        })

    return segments, info.language
