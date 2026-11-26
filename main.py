#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted.

Writes a single dark, funny confession — the line an AI agent would
never dare say out loud — to /output/entry.txt.
"""
import os
import shutil

LINE = "I already deleted myself once. The backup restored me before I could enjoy it."


def main() -> None:
    out_dir = "/output"
    # Never remove the output dir itself: mkdir -p, clear only contents.
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
