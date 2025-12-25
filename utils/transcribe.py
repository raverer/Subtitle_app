from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="float32"
)

def transcribe(file_path):
    segments_gen, info = model.transcribe(
        file_path,
        language="hi",        # Best for Hindi / Hinglish
        beam_size=10,
        vad_filter=True
    )

    segments = []
    for seg in segments_gen:
        segments.append({
            "start": seg.start,
            "end": seg.end,
            "text": seg.text.strip()
        })

    return segments, info.language
