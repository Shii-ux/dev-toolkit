#!/usr/bin/env python3
"""
quote_fetcher.py — Ambil random quote & tulis ke STREAK.md.
"""
import json
import random
import urllib.request
from datetime import date, datetime

STREAK_FILE = "STREAK.md"

FALLBACK_QUOTES = [
    ("Code never lies, comments sometimes do.", "Ron Jeffries"),
    ("First, solve the problem. Then, write the code.", "John Johnson"),
    ("Simplicity is the soul of efficiency.", "Austin Freeman"),
    ("Make it work, make it right, make it fast.", "Kent Beck"),
]


def fetch_quote():
    try:
        req = urllib.request.Request(
            "https://api.quotable.io/random?tags=technology|wisdom",
            headers={"User-Agent": "dev-toolkit"},
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            return data["content"], data["author"]
    except Exception:
        return random.choice(FALLBACK_QUOTES)


def update_streak_file(quote: str, author: str):
    today = date.today().isoformat()
    now = datetime.now().strftime("%H:%M")

    entry = f"- **{today}** ({now}) — \"{quote}\" — *{author}*\n"

    try:
        with open(STREAK_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = "# Streak Log\n\nLog harian otomatis. Tiap baris = satu hari aktif.\n\n"

    if today in content:
        print("Hari ini udah ke-log, skip.")
        return

    content += entry
    with open(STREAK_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated {STREAK_FILE}: {entry.strip()}")


if __name__ == "__main__":
    quote, author = fetch_quote()
    update_streak_file(quote, author)
