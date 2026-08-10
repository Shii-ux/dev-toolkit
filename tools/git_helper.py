#!/usr/bin/env python3
"""
git_helper.py — Shortcut buat add + commit + push cepat.

Contoh:
    python git_helper.py "fix: rapihin rename_bulk.py"
    python git_helper.py --auto     # commit message otomatis pakai timestamp
"""
import argparse
import subprocess
import sys
from datetime import datetime


def run(cmd: list[str]) -> None:
    print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        sys.exit(result.returncode)


def main():
    parser = argparse.ArgumentParser(description="Commit + push cepat.")
    parser.add_argument("message", nargs="?", help="Pesan commit")
    parser.add_argument("--auto", action="store_true", help="Pakai pesan otomatis (timestamp)")
    parser.add_argument("--no-push", action="store_true", help="Cuma commit, jangan push")

    args = parser.parse_args()

    if args.auto:
        msg = f"chore: update {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    elif args.message:
        msg = args.message
    else:
        print("Kasih pesan commit, atau pakai --auto.")
        sys.exit(1)

    run(["git", "add", "-A"])
    run(["git", "commit", "-m", msg])
    if not args.no_push:
        run(["git", "push"])


if __name__ == "__main__":
    main()
