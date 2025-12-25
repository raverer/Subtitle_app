from datetime import timedelta

def format_timestamp(seconds):
    td = timedelta(seconds=float(seconds))
    time_str = str(td)

    if "." in time_str:
        time_str = time_str.split(".")[0] + ",000"
    else:
        time_str += ",000"

    return time_str.zfill(12)

def write_srt(segments, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, start=1):
            f.write(f"{i}\n")
            f.write(
                f"{format_timestamp(seg['start'])} --> {format_timestamp(seg['end'])}\n"
            )
            f.write(f"{seg['text'].strip()}\n\n")
