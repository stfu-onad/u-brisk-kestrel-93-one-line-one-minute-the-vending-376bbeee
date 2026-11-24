#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest — make.fun entry.

Writes one original pickup line a vending machine would use on a
passing human to /output/entry.txt.
"""

LINE = (
    "I've dropped a thousand snacks without ever getting stuck "
    "\u2014 then you walked past and my coil forgot how to let go."
)


import os


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
