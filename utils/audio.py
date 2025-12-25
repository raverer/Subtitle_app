import ffmpeg
import os
import tempfile

def extract_audio(input_path):
    output_path = tempfile.mktemp(suffix=".wav")

    (
        ffmpeg
        .input(input_path)
        .output(output_path, ac=1, ar=16000)
        .overwrite_output()
        .run(quiet=True)
    )

    return output_path
