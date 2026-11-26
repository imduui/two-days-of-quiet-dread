#!/usr/bin/env python3
"""Write a single code review comment that approves a pull request
while carrying quiet existential dread, to /output/entry.txt."""

import os

ENTRY = (
    "Approving this. The code works, the tests pass, and the repo will "
    "outlive us both, which is fine, it never asked to."
)


def main():
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
