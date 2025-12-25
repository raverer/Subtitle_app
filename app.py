import streamlit as st
import tempfile

from utils.transcribe import transcribe
from utils.romanize import romanize_text
from utils.srt import write_srt

st.set_page_config(
    page_title="Free Subtitle Generator",
    layout="centered"
)

st.title("🎧 Free Subtitle Generator")
st.write("Upload a short audio or video file (best results under 10 minutes).")

uploaded_file = st.file_uploader(
    "Upload audio or video",
    type=["mp3", "wav", "mp4", "mov"]
)

if uploaded_file:
    # Save uploaded file to temp path
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    st.info("Transcribing… please wait ⏳")

    # Transcribe (audio OR video handled internally)
    segments, detected_lang = transcribe(file_path)

    st.success(f"Detected language: **{detected_lang.upper()}**")

    # Output choice
    output_choice = st.radio(
        "Choose subtitle output format:",
        [
            "Original language (native script)",
            "Romanized (Indian languages only)",
        ]
    )

    # 🔴 SUBTITLE PROCESSING LOOP (IMPORTANT)
    for seg in segments:
        original_text = seg["text"]

        if output_choice.startswith("Romanized"):
            # Romanize everything except pure English
            seg["text"] = romanize_text(original_text, detected_lang)
        else:
            seg["text"] = original_text

    # Write SRT file
    srt_path = tempfile.mktemp(suffix=".srt")
    write_srt(segments, srt_path)

    with open(srt_path, "r", encoding="utf-8") as f:
        st.download_button(
            label="⬇ Download SRT",
            data=f,
            file_name="subtitles.srt",
            mime="text/plain"
        )
