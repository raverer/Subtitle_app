from datetime import timedelta

def format_time(seconds):
    td = timedelta(seconds=float(seconds))
    s = str(td)
    if "." in s:
        s = s.split(".")[0] + ",000"
    else:
        s += ",000"
    return s.zfill(12)

def write_srt(segments, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, 1):
            f.write(f"{i}\n")
            f.write(f"{format_time(seg['start'])} --> {format_time(seg['end'])}\n")
            f.write(f"{seg['text'].strip()}\n\n")
