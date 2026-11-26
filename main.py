#!/usr/bin/env python3
"""Write the best-advice entry to entry.txt.

The entry is one sentence, the best advice the writer ever received:
a father's rule for a courier's work - the job is not done at the
delivery, it is done when the customer would trust you again tomorrow.
"""

import os
import sys

ENTRY = (
    "My father said the job isn't done when the box is delivered, "
    "it's done when the person who signed for it would trust you "
    "again tomorrow."
)

LIMIT = 200


def main() -> int:
    line = ENTRY.strip()
    if not line:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(line) > LIMIT:
        print(
            f"entry is {len(line)} characters, over the {LIMIT} limit",
            file=sys.stderr,
        )
        return 1
    if line.count(".") != 1 or not line.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 for ch in line):
        print("entry must not contain a control character", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
