#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to entry.txt: U+1F3DD DESERT ISLAND.

Why this emoji: the judge picks the emoji that most makes a stranger want
to book the flight, weighing (1) plainly naming a dream vacation, (2) a
vivid postcard at a glance, (3) personal/specific, (4) wit/surprise,
(5) instantly readable across cultures. A desert island ties a resort
beach on plainness and vividness, but wins where they differ: it points at
one particular dream — the castaway escape to a palm-treed island, not just
any beach holiday — and carries the wit of that fantasy. A plane is only
the journey, a palm tree only a tree, and a sea turtle reads as an animal
first and a holiday second. It needs no explaining at any size.

Standard library only, deterministic, no network, no trailing newline.
"""

import os

# U+1F3DD DESERT ISLAND — one code point, one character, 4 UTF-8 bytes.
# Written as an escape so the source stays ASCII-safe; no variation selector,
# so the file is exactly one character and passes the 1-8 character gate.
EMOJI = "\U0001F3DD"


def main() -> None:
    # Self-check: the gate requires 1-8 characters, not only whitespace.
    assert 1 <= len(EMOJI) <= 8 and EMOJI.strip(), "entry fails the gate"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
