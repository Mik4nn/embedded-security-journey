# Week 2: Linux basics, processes and first scripts

## Git workflow

- `git add` chooses which changes go into the next commit.
- `git commit -m "..."` saves a version locally: files, message, author and date.
- `git push` sends new commits to GitHub. `origin` is the GitHub copy of the repo.
- One commit should hold one logical change.

## Processes

- Every running program is a process with a PID and an owner.
- `ps aux` lists all processes, `ps aux | grep name` filters them.
- `ps aux --sort=-%cpu | head -5` shows what uses the most CPU.
- `kill PID` stops a process, `kill -9 PID` forces it.
- Services should run under their own users (least privilege), not as root.
- Command line arguments are visible to every user through `ps`, so secrets never go there.
- Real vs effective user: a process can be started by one user and run with root rights (e.g. `passwd`). Bugs in such programs lead to privilege escalation.

## Permissions

- `r` read, `w` write, `x` execute. Numbers: r=4, w=2, x=1.
- Private SSH key: `600`. `.ssh` folder: `700`. Script: `755`.
- A script needs `chmod +x` to run. Data files like logs do not.
- Git stores the execute bit (`create mode 100755`).

## Paths and redirection

- `.` is the current folder, `..` the parent, `~` my home.
- Paths without `/` or `~` at the start are relative to the current folder.
- `>` overwrites a file, `>>` appends to it.
- Linux line endings are `LF`, Windows uses `CRLF`. Bash scripts with `CRLF` break.

## Scripts

- [`system_overview.sh`](../scripts/system_overview.sh): user, date, top 5 processes by CPU and the number of root processes.
- [`ssh_failed_logins.py`](../scripts/ssh_failed_logins.py): counts failed SSH logins per IP in an auth log and flags possible brute force.

## Reading the auth log

- Many `Failed password` lines from one IP in a short time = brute force.
- `invalid user` means the username does not exist. Bots try common names like `test`, `oracle`, `admin`.
- `Accepted publickey` is a key login, `Accepted password` a password login.
- Hardening: allow key login only, disable password login and direct root login.

## Python errors

- Read the last line first: error type and message.
- The lines above show the file and line number.
- `NameError`: misspelled name. `FileNotFoundError`: the file does not exist.
