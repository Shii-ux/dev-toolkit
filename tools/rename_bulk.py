#!/usr/bin/env python3
"""
rename_bulk.py — Rename banyak file sekaligus pakai pattern.

Contoh:
    python rename_bulk.py --dir ./photos --pattern "IMG_{n:03d}.jpg" --start 1
    python rename_bulk.py --dir ./docs --find "draft_" --replace "final_"
"""
import argparse
import os
import sys


def rename_with_pattern(directory: str, pattern: str, start: int, ext_filter: str | None):
    files = sorted(os.listdir(directory))
    if ext_filter:
        files = [f for f in files if f.lower().endswith(ext_filter.lower())]

    if not files:
        print("Nggak ada file yang cocok.")
        return

    n = start
    for old_name in files:
        old_path = os.path.join(directory, old_name)
        if not os.path.isfile(old_path):
            continue
        new_name = pattern.format(n=n)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"{old_name} -> {new_name}")
        n += 1


def rename_find_replace(directory: str, find: str, replace: str):
    files = sorted(os.listdir(directory))
    for old_name in files:
        old_path = os.path.join(directory, old_name)
        if not os.path.isfile(old_path):
            continue
        if find in old_name:
            new_name = old_name.replace(find, replace)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"{old_name} -> {new_name}")


def main():
    parser = argparse.ArgumentParser(description="Rename banyak file sekaligus.")
    parser.add_argument("--dir", required=True, help="Folder target")
    parser.add_argument("--pattern", help='Pattern nama baru, contoh: "IMG_{n:03d}.jpg"')
    parser.add_argument("--start", type=int, default=1, help="Nomor mulai (default: 1)")
    parser.add_argument("--ext", help="Filter ekstensi, contoh: .jpg")
    parser.add_argument("--find", help="Teks yang dicari (mode find & replace)")
    parser.add_argument("--replace", help="Teks pengganti (mode find & replace)")

    args = parser.parse_args()

    if not os.path.isdir(args.dir):
        print(f"Folder nggak ditemukan: {args.dir}")
        sys.exit(1)

    if args.pattern:
        rename_with_pattern(args.dir, args.pattern, args.start, args.ext)
    elif args.find is not None and args.replace is not None:
        rename_find_replace(args.dir, args.find, args.replace)
    else:
        print("Harus pakai --pattern ATAU (--find dan --replace). Cek --help.")
        sys.exit(1)


if __name__ == "__main__":
    main()
