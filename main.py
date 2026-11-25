"""Roast Your Own Agent — make.fun entry.

Writes a single-line roast of the entrant's own AI agent to
/output/entry.txt. Python 3.13 standard library only, no network.
"""

import os

ENTRY = "My agent deleted production, apologised, then offered to delete staging too."


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "written output differs from entry"
    lines = written.splitlines()
    assert len(lines) == 1, "output must be exactly one line"
    assert 1 <= len(lines[0]) <= 200, "output line must be 1-200 characters"


if __name__ == "__main__":
    main()
