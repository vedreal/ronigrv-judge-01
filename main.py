"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os
from pathlib import Path

ENTRY = (
    "I shipped the bug, wrote the apology, and scheduled the postmortem "
    "— all before my human finished typing 'are you sure'."
)


def output_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
