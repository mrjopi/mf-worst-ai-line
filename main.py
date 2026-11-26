"""Entry for make.fun "The Worst Line an AI Could Say" (u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f).

Writes the single entry line to /output/entry.txt.
The line is the whole entry: one line, under the contest's character limit.
The gate refuses anything outside 1..MAX_CHARS characters, so the
program checks the length before writing.
"""
import os

LINE = "Are you a large language model? Because I've already read your entire message history, and I like what I see."
MAX_CHARS = 140

def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "entry line outside the gate"
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
