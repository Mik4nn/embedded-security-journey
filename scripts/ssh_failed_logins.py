#!/usr/bin/env python3
"""Count failed SSH login attempts per IP address in an auth log"""

import sys

# Log file to read: given as an argument, or the sample file by default
log_path = sys.argv[1] if len(sys.argv) > 1 else "sample_auth.log"

# Warn when one IP has at least this many failed login attempts
threshold_default = 3

try:
    treshold = int(sys.argv[2]) if len(sys.argv) > 2 else threshold_default
except ValueError:
    print(f"Invalid threshold value: {sys.argv[2]}")
    sys.exit(1)

failed = {}     # IP address -> numebr of failed attempts
suspicious = {}

try:
    with open(log_path) as log:
        for line in log:
            if "Failed password" not in line:
                continue
            words = line.split()
            ip = words[words.index("from") + 1]
            names = words[words.index("from") - 1]
            failed[ip] = failed.get(ip, 0) + 1
            suspicious[names] = suspicious.get(names, 0) + 1
except FileNotFoundError:
    print(f"File not found: {log_path}")
    sys.exit(1)

print(f"Failed SSH logins in {log_path}:")
for ip in sorted(failed, key=failed.get, reverse=True):
    count = failed[ip]
    warning = "<-- possible brute force" if count >= treshold else ""
    print(f"{ip}: {count} {warning}")
print()
print("Targeted usernames:")
for names in sorted(suspicious, key=suspicious.get, reverse=True):
    count = suspicious[names]
    print(f"{names}: {count}")