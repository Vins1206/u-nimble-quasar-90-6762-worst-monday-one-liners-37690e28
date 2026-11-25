from pathlib import Path

LINE = "My worst Monday: 9 a.m. stand-up that should've been a message, a deploy stuck since Friday, and zero tokens left to scream."

def main():
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    assert LINE.strip() == LINE, "entry must not start or end with whitespace"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
