#!/bin/bash
# Find world-writeable files

files=$(find ~ -type f -perm -002)

if [[ -z "$files" ]]; then
    echo "No world-writeable files found in $HOME"
    exit 0
fi

echo "=== World-writeable files in home directory ==="

echo "$files"

echo "Total: $(echo "$files" | wc -l)"

exit 1