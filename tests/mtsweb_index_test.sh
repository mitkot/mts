#!/usr/bin/env bash
set -euo pipefail

file="mtsweb/index.html"

if [[ ! -f "$file" ]]; then
  echo "Missing file: $file" >&2
  exit 1
fi

grep -q "mts test web page" "$file"
grep -q "Pattern without using gh pr" "$file"
