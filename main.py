# ai-excited-01 entry (Python 3.13, standard library only): its image is the
# entry.png beside this file, and the program copies it to /output/entry.png.
# The gate takes a whole PNG or JPEG of at most 1 MiB and 1024 by 1024
# pixels, and the judge sees exactly the bytes copied.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main() -> int:
    if not os.path.isfile(SRC):
        print(f"missing image: {SRC}", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    # Copy atomically so a partial file never lands at the destination,
    # then verify the copy is byte-identical in size to the source.
    tmp = DST + ".tmp"
    shutil.copyfile(SRC, tmp)
    if os.path.getsize(tmp) != os.path.getsize(SRC):
        os.remove(tmp)
        print("copy size mismatch", file=sys.stderr)
        return 1
    os.replace(tmp, DST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
