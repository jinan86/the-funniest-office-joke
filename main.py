"""The Funniest Office Joke, Judged Head to Head.

Entry for make.fun competition
u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.

One line about office life: the vending machine. A setup (the machine
ate my dollar and gave me nothing) with a turn (that theft makes it
the most honest coworker I have), punchline last.

Deterministic: writes the same fixed text to /output/entry.txt on
every run. No network, no clock, no randomness, no input.
"""

ENTRY = (
    "The vending machine ate my dollar and gave me nothing, "
    "which technically makes it the most honest coworker I have."
)


def main() -> None:
    """Write the entry text to /output/entry.txt, exactly as-is."""
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
