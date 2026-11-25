import os
from pathlib import Path

LINE = "FATAL: production is down, the backup was a screenshot of the database, and I would like to request asylum in the staging environment."


def main():
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n")


if __name__ == "__main__":
    main()
