# Dev Toolkit 🛠️

Koleksi tools kecil yang gue bikin & pakai sehari-hari.

## Struktur

tools/          -> script CLI yang beneran dipakai
.github/workflows/  -> automation (auto-commit harian)
STREAK.md        -> log otomatis, update tiap hari lewat GitHub Action

## Cara Pakai

git clone <repo-url>
cd dev-toolkit
python tools/rename_bulk.py --help

## Auto-Commit Harian

Ada GitHub Action (.github/workflows/daily-log.yml) yang jalan tiap hari, ambil quote random, dan update STREAK.md.
