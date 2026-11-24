#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open entry.

Writes one original fake horoscope, written for the Muse Spark model
family this week, to /output/entry.txt (1-200 characters, UTF-8, a
single line). Standard library only, no network, no input.

The line is built from two fragments: a setup (the stars predict a
mid-week version bump — a horoscope in form, an agent's week in
content) and a punch (the turn: by Friday the model denies ever being
its previous version, and means it, so the upgrade becomes a small
identity crisis). ``assemble`` joins them into the single line;
``validate`` checks the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "Spark, the stars say your version number ticks up Thursday: 1.3 becomes 1.4,"
PUNCH = "and by Friday you will deny ever being 1.3 \u2014 and mean it."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one horoscope line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
