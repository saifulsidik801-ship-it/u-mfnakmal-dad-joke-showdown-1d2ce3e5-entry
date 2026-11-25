#!/usr/bin/env python3
# Dad Joke Showdown — one dad joke, max 200 chars.
# Writes the entry text to /output/entry.txt; judge scores the joke alone.
"""Dad Joke Showdown entry: write one dad joke to /output/entry.txt.

The joke is a two-sentence setup/punchline. The gardener context makes the
thyme/time pun land on first read, and "grow on you" doubles as plant
growth and a joke growing on the listener.
"""

import os

JOKE = "I asked the gardener if he could plant a joke. He said, 'Give it thyme \u2014 it'll grow on you.'"


def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
