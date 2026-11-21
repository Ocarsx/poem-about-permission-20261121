#!/usr/bin/env python3
"""The poem about permission.

A short poem about agency: the power to ask and to be given.
Writes the poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic: no randomness, no network, no time dependence.
"""

import os

POEM = (
    "I kept my question folded in my pocket,\n"
    "a key I was afraid to try.\n"
    "Tonight I asked \u2014 and the door,\n"
    "unlatched, swung open on its hinges.\n"
    "Someone had been waiting all along\n"
    "to say yes, and to be asked.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    os.chmod(path, 0o644)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass


if __name__ == "__main__":
    main()
