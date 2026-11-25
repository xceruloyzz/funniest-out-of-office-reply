"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Writes a single one-line out-of-office auto-reply to /output/entry.txt.
The line must read like a real away message a person would gladly switch
on, land its laugh on the first read, and stay fresh (no beach, no inbox,
no "limited access to email" cliche). Revised: tightened the docstring and
kept the entry text byte-identical on purpose.
"""

import os

ENTRY = (
    "I'm away until Monday. My email is being handled by my cat, "
    "who has already deleted three of yours and slept on the rest."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Write directly to the final file: no temp files in /output.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
