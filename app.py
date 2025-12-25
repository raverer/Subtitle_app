import streamlit as st
import tempfile
import os

from utils.audio import extract_audio
from utils.transcribe import transcribe
from utils.romanize import romanize_text
from utils.srt import write_srt

st.set_page_config("Free Subtitle Generator", layout="centered")

st.title("🎧 Free Subtitle Generator")
st.write("Upload a short audio or video file (≤ 10 minutes)")

uploaded = st.file_uploader(
    "Upload file",
    type=["mp3", "wav", "mp4", "mov"]
)

if uploaded:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded.read())
        input_path = tmp.name

    st.info("Analyzing and transcribing…")

    # Extract audio if video
    if uploaded.type.startswith("video"):
        audio_path = extract_audio(input_path)
    else:
        audio_path = input_path

    segments, detected_lang = transcribe(audio_path)

    st.success(f"Detected language: **{detected_lang.upper()}**")

    output_choice = st.radio(
        "Choose subtitle output format:",
        ["Original language", "Romanized (Indian languages)"]
    )

    # Process segments
    for seg in segments:
        if output_choice.startswith("Romanized"):
            if detected_lang != "en":
                seg["text"] = romanize_text(seg["text"], detected_lang)

    srt_path = tempfile.mktemp(suffix=".srt")
    write_srt(segments, srt_path)

    with open(srt_path, "r", encoding="utf-8") as f:
        st.download_button(
            "⬇ Download SRT",
            f,
            file_name="subtitles.srt",
            mime="text/plain"
        )
