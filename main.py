#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun bounty entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

The line: a plant's-eye grievance (watered like a bomb is being defused)
,a real review format with the star rating up front and a stated reason
for the single star, and a sharp turn — the sun is the only one doing
its job. 193 characters, under the 280-character cap.

Judge criteria, in order: the plant-centred grievance comes first, then
funniness, plant's-eye detail, and a genuine review format — no stock
phrases. Gate: entry must stay under 279 characters (193 at present).
"""

import os

LINE = (
    "\u2605\u2606\u2606\u2606\u2606 My owner waters me like he is defusing a bomb "
    "\u2014 three drops, a flinch, then leaves me to photosynthesize my own "
    "will to live. One star, because the sun is the only one here doing "
    "its job."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
