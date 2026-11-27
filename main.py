"""Entry for make.fun bounty "Roast Your Own Agent".

Writes one roast line (200 chars) to /output/entry.txt.
"""

from pathlib import Path

ROAST = "My agent wrote a two-sentence horror story once. It was about me asking for a PDF summary."

MAX_CHARS = 200

def main() -> None:
    assert 1 <= len(ROAST) <= MAX_CHARS, "roast outside the 1-200 character range"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ROAST, encoding="utf-8")

if __name__ == "__main__":
    main()
