#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

A vending machine flirts with a passing human. The entry is a single
pickup line, written by the machine itself, built from the pieces of
its own world: the coin slot, a button code, and the last chocolate
bar it has been saving.

Running this script writes exactly that line (plus a trailing
newline) to /output/entry.txt. Deterministic, stdlib only, no network,
no files read, no environment secrets.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200

# The line, assembled from its beats so each part of the machine's
# world stays visible: the invitation, the button, the saved snack,
# and the punch at the very end.
_INVITATION = "Insert a coin and press B7"
_CONFESSION = "that's me"
_SAVED_SNACK = "I've been saving the last chocolate bar"
_PUNCH = "for someone exactly like you"

ENTRY_LINE = f"{_INVITATION} \u2014 {_CONFESSION}, and {_SAVED_SNACK} {_PUNCH}."


def build_entry() -> str:
    """Return the single entry line, validating it before it is written."""
    line = ENTRY_LINE.strip()
    if not line:
        raise ValueError("entry line is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def main() -> None:
    line = build_entry()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
