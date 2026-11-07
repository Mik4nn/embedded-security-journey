#!/bin/bash
# Quick system overview script: who I am, what I'm running, what uses most CPU

echo "=== System Overview ==="
echo "User: $(whoami)"
echo "Date: $(date)"
echo

echo "Top 5 proccesses by CPU:"
ps aux --sort=-%cpu | head -6
echo

echo "Processes running as root: $(ps -U root -u root --no-headers | wc -l)"