#!/bin/bash
# tools/streak_stats.sh
# Ngitung total hari yang udah ke-log di STREAK.md

FILE="STREAK.md"

if [ ! -f "$FILE" ]; then
  echo "STREAK.md nggak ketemu."
  exit 1
fi

TOTAL=$(grep -c "^- \*\*" "$FILE")
FIRST=$(grep "^- \*\*" "$FILE" | head -1 | grep -oP '\d{4}-\d{2}-\d{2}')
LAST=$(grep "^- \*\*" "$FILE" | tail -1 | grep -oP '\d{4}-\d{2}-\d{2}')

echo "Total hari ke-log: $TOTAL"
echo "Mulai dari: $FIRST"
echo "Terakhir: $LAST"
