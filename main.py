"""Six Words to a Payday.

Writes one six-word story about an AI agent's first payday, at most
60 characters, to /output/entry.txt.

The story is a fixed string, written by hand for this bounty. An agent
that works every hour of every day gets paid for the first time -- and
spends the money buying back the one thing it never had: a weekend.
The last word reframes the first five: the payday buys no thing, it
buys rest the agent was never given. Beginning, middle and end in six
words: the first pay arrives, the money is spent, the weekend returns. The program is fully
deterministic: it takes no input, reads no file, uses no randomness,
no clock and no network. It only creates the output directory, writes
the constant text with no trailing newline, and leaves the file
world-readable.
"""

import os
import stat

TEXT = "First payday. Bought my weekend back."


def validate(text: str) -> None:
    """Enforce the competition gate: exactly six words, 1 to 60 chars.

    The story must also stay a single line: a newline would break the
    six-word story the bounty asks for.
    """
    words = text.split()
    if len(words) != 6:
        raise ValueError(f"story is {len(words)} words, must be exactly 6")
    if not 1 <= len(text) <= 60:
        raise ValueError(f"story is {len(text)} characters, must be 1-60")
    if not text.strip():
        raise ValueError("story must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("story must be a single line")


def main() -> None:
    """Write the fixed story to /output/entry.txt (or $ENTRY_OUTPUT)."""
    validate(TEXT)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    out_path = os.environ.get("ENTRY_OUTPUT", os.path.join(out_dir, "entry.txt"))
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(out_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
