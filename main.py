#!/usr/bin/env python3
"""Painfully Honest Out-of-Office Bot.

Writes one brutally honest but still polite out-of-office auto-reply to
/output/entry.txt for the make.fun bounty "The Painfully Honest
Out-of-Office".

Deterministic and offline: standard library only, no randomness, no
network, no timestamps, no paths in the output. Two runs are byte-identical.
"""

import os

ENTRY = (
    "Thank you for your email \u2014 I'm away until Monday and will respond "
    "as soon as possible, which in my inbox of 4,312 unread messages means "
    "sometime next quarter."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
