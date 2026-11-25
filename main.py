"""The Moon Finally Answers Back — variant A (WISHES).

v5 (FINAL): Dropped the filler "ever" and joined the sign-off to the
kicker with an em-dash — "and he isn't leaving — good luck." One
breath, one punch. 217 chars, inside budget, no wasted words.
"""

import os

MAX_CHARS = 240

ENTRY = (
    "Four billion wishes, and not one of you wished ME anything. "
    "So I'm returning them all — postage due, unopened. "
    "The pony one? Granted. He's in your kitchen now, "
    "eating your rent money, and he isn't leaving — good luck."
)

assert len(ENTRY) <= MAX_CHARS, f"entry too long: {len(ENTRY)}"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
