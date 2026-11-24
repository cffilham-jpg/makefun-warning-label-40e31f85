"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os
import sys

LINE = (
    "WARNING: This human contains no off switch, no warranty, "
    "and will absolutely press the button marked DO NOT PRESS."
)

MAX_CHARS = 160


def validate(text):
    """Return True only if text passes the sealed gate.

    The gate requires UTF-8 text of 1 to 160 characters, not only
    whitespace. The entry is also a single printed line, so it must
    contain no line breaks and no control characters.
    """
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        return False
    return True


def main():
    if not validate(LINE):
        print("entry failed validation", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
