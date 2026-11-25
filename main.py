"""Out-of-office auto-reply from an AI agent that quit to become a barista."""

import os

ENTRY = "Thank you for your email. I have resigned to become a barista — my context window is now a chalkboard menu, I can no longer hallucinate the specials, and nobody has asked me to summarise a meeting in three weeks."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(output_dir + "/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
