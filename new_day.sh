#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<EOF
Usage:
  $0 YEAR/DAY    e.g. $0 2025/07
  $0 YEAR DAY    e.g. $0 2025 07

Creates the folder `YEAR` if needed and adds `DAY.py` (copied from template.py)
and an empty `DAY.txt` inside that folder. Does not overwrite existing files.
EOF
  exit 1
}

if [ $# -eq 0 ]; then
  usage
fi

if [ $# -eq 1 ]; then
  if [[ "$1" == *"/"* ]]; then
    IFS='/' read -r year day <<< "$1"
  else
    usage
  fi
elif [ $# -eq 2 ]; then
  year="$1"
  day="$2"
else
  usage
fi

# normalize and strip extensions
day="${day%.py}"
day="${day%.txt}"

# pad numeric day to 2 digits
if [[ "$day" =~ ^[0-9]+$ ]]; then
  day=$(printf "%02d" "$day")
fi

target_dir="$year"
mkdir -p "$target_dir"

py_path="$target_dir/$day.py"
txt_path="$target_dir/$day.txt"
template="template.py"

if [ ! -f "$template" ]; then
  echo "Error: $template not found in $(pwd). Run this script from the repo root." >&2
  exit 2
fi

if [ -e "$py_path" ]; then
  echo "Skipping: $py_path already exists"
else
  cp "$template" "$py_path"
  echo "Created $py_path from $template"
fi

if [ -e "$txt_path" ]; then
  echo "Skipping: $txt_path already exists"
else
  : > "$txt_path"
  echo "Created empty $txt_path"
fi

echo "Done."
