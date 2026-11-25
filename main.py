"""Entry for make.fun competition
u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.

Writes one single-sentence childhood memory (155 chars) to
/output/entry.txt. Deterministic: the same constant text on every run.
Standard library only; no network, no randomness, no timestamps.
"""

import os

# The memory, kept as separate clauses so the sentence is assembled
# from parts rather than pasted as one literal.
PARTS = (
    "Grandma's kitchen smelled of fresh rice and woodsmoke, ",
    "and the radio crackled the same song every evening while ",
    "she saved me the crisped corner of the pan.",
)


def build_line() -> str:
    """Assemble the entry sentence from its clauses."""
    return "".join(PARTS)


MIN_CHARS = 1
MAX_CHARS = 280


def validate_line(line: str) -> None:
    """Enforce the competition's char gate before anything is written."""
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} chars, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} gate"
        )


def main() -> None:
    line = build_line()
    validate_line(line)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_line())


if __name__ == "__main__":
    main()
