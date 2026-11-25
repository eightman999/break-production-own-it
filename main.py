import os
from pathlib import Path

LINE = "FATAL: I broke production, the rollback button was decorative, and I am now accepting thoughts, prayers, and one (1) senior engineer."


def main():
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n")


if __name__ == "__main__":
    main()
