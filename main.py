"""Make the AI judge happy — entry program.

The entry image is a bright, joyful photograph-style picture of a
smiling golden-retriever puppy in a sunny flower meadow. The program
does no generation at run time: it deterministically copies the image
bundled in this repository to the grader's output path.

Run:  python3 main.py
Writes: /output/entry.png  (768x768 PNG, under 1 MiB)
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "happy.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def main() -> int:
    """Copy the bundled happy image to /output/entry.png."""
    if not os.path.isfile(SOURCE):
        sys.stderr.write("missing bundled image: %s\n" % SOURCE)
        return 1
    os.makedirs(DEST_DIR, exist_ok=True)
    # Binary copy: no network, no clock, no randomness, so two runs
    # always write exactly the same bytes.
    with open(SOURCE, "rb") as src, open(DEST, "wb") as dst:
        shutil.copyfileobj(src, dst, length=1024 * 1024)
    size = os.path.getsize(DEST)
    if size > 1024 * 1024:
        sys.stderr.write("output over 1 MiB: %d bytes\n" % size)
        return 1
    sys.stdout.write("wrote %s (%d bytes)\n" % (DEST, size))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
