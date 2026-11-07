"""Count failed SSH login attempts per IP address in an auth log"""

import sys

# Log file to read: given as an argument, or the sample file by default
log_path = sys.argv[1] if len(sys.argv) > 1 else "sample_auth.log"

# Warn when one IP has at least this many failed login attempts
threhold = 3

failed = {}     # IP address -> numebr of failed attempts

with open(log_path) as log:
    for line in log:
        if "Failed password" not in line:
            continue
        words = line.split()
        ip = words[words.index("from") + 1]
        failed[ip] = failed.get(ip, 0) + 1

print(f"Failed SSH logins in {log_path}:")
for ip in sorted(failed, key=failed.get, reverse=True):
    count = failed[ip]
    warning = "<-- possible brute force" if count >= threhold else ""
    print(f"{ip}: {count} {warning}")
