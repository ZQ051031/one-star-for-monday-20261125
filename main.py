"""One Star for Monday: write a one-star restaurant review of Monday.

The entry is a single plain-text line, at most 25 words, written to
/output/entry.txt with no trailing newline. The program is fully
deterministic: it always writes the same fixed line, and it checks
the line against the competition limits (1-180 characters, at most
25 words, single line) before writing it out.
"""

import os

ENTRY = (
    "One star. Monday seated me by the bathroom, served cold coffee "
    "and a 6 a.m. alarm, then charged me my whole weekend."
)


def main():
    words = ENTRY.split()
    assert 1 <= len(ENTRY) <= 180, "entry must be 1-180 characters"
    assert len(words) <= 25, "entry must be at most 25 words"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
