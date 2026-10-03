# Git + TortoiseGit for this repo — step by step

Written for someone who's never used Git. Follow in order the first time;
after that you only need section 4 (Day-to-day workflow).

## 1. Install the tools (once)

1. [Git for Windows](https://git-scm.com/downloads) — default options are fine.
2. [Git LFS](https://git-lfs.com/) — download, run the installer.
3. [TortoiseGit](https://tortoisegit.org/) — install, let it use the Git you
   just installed. Reboot if asked.
   - **If it stops with an error about "Microsoft Visual C++ 2015-2022
     Redistributable":** install that first, then re-run the TortoiseGit
     installer.
     - https://aka.ms/vs/17/release/vc_redist.x64.exe (normal 64-bit Windows)
     - Install → Close, no options to change, then retry TortoiseGit.
     - Still complaining? Also install
       https://aka.ms/vs/17/release/vc_redist.x86.exe and retry.
4. Make a free [GitHub](https://github.com) account if needed, and ask the
   repo owner to add you as a collaborator.

## 2. Clone the repo (once)

1. Make a folder, e.g. `C:\FSUK\`.
2. Right-click inside it → **Git Clone...**
3. Paste the repo URL (`https://github.com/<owner>/FSUK-BMS.git`).
4. Click OK.
5. Open Command Prompt / PowerShell **inside the cloned folder**, run:
   ```
   git lfs install
   ```
   One-time per computer. Without this, the Altium files you download are
   just tiny placeholder text files Altium can't open.
6. Then:
   ```
   git lfs pull
   ```
   Downloads the real Altium/PDF files. Check `BMS-Master\Sheets\` and
   `BMS-Module\Sheets\` actually contain `.SchDoc` files before opening
   Altium.
7. Set your Git identity (once per computer):
   ```
   git config --global user.name "your-github-username"
   git config --global user.email "you@example.com"
   ```
8. Sign in to GitHub (once per computer):
   ```
   git credential-manager github login
   ```
   A browser window opens — approve it. You also need to actually be added
   as a collaborator, or pushes get rejected.

## 3. Why you'll "lock" files before editing

`.SchDoc`, `.PcbDoc`, `.SchLib`, `.PcbLib` are binary — Git can't merge two
people's edits to the same file. Two people editing `Top.SchDoc` and both
pushing means a conflict Git can't auto-resolve.

Fix: **lock the file before editing it.** Makes it read-only for everyone
else until you unlock it.

## 4. Day-to-day workflow

**Before starting work:**

1. Right-click the repo folder → **TortoiseGit → Pull.**

**Before editing a specific file:**

2. Right-click that file → **TortoiseGit → Lock.**
   - Already locked by someone else? Don't edit it — message them, work on
     something else until they unlock it.
3. Edit in Altium, save.

**After editing:**

4. Right-click the repo folder → **TortoiseGit → Commit...**
   - Tick the changed files.
   - Write a message following section 6's format.
   - Commit.
5. Right-click the repo folder → **TortoiseGit → Push.**
6. Right-click the file(s) you locked → **TortoiseGit → Unlock.**

Loop: **Pull → Lock → Edit → Commit → Push → Unlock.**

## 5. Rules of thumb

- **Never sit on a lock.** Lock right before editing, unlock right after
  pushing.
- **`Top.SchDoc` in each project is the one everyone wants.** Lock it, edit,
  push quickly — don't leave it locked while doing something else.
- **Pull before every session** — editing an old version means redoing the
  work on top of the latest one anyway.
- **Push rejected** ("non-fast-forward"): someone pushed first. Pull, then
  push again.
- **Commit messages**: see section 6.

## 6. Commit message format

`<type>(<board>): <summary>` — scope is `master`, `module`, or omitted for
changes not tied to one board.

| Type | For |
|---|---|
| `sch` | Schematic edits (`.SchDoc`) |
| `pcb` | PCB layout edits (`.PcbDoc`) |
| `lib` | Library edits (`.SchLib`/`.PcbLib`) |
| `fix` | Correcting a mistake in a previous commit |
| `docs` | README / `Docs/` changes |
| `ref` | `Reference Docs/` additions or reorganization |
| `repo` | Repo config — `.gitignore`, `.gitattributes`, OutJob setup, git/LFS setup |

Rules:

1. Imperative mood — "Add", "Fix", "Move", not "Added"/"Fixed".
2. Summary line ≤ 72 chars, no trailing period.
3. Name the sheet/file when the type alone doesn't make it obvious.
   `BMS-Master/Sheets/Connectors.SchDoc` and `BMS-Module/Sheets/Connectors.SchDoc`
   both exist — the `(board)` scope disambiguates, the filename alone doesn't.
4. Body text (blank line, then free text) only when the summary doesn't
   explain *why*.

Examples:

- `sch(master): add CAN transceiver to CAN.SchDoc`
- `sch(module): add balancing FET to Balancing.SchDoc`
- `fix(master): correct balancing FET footprint`
- `docs(master): add STM32G474 selection rationale`
- `ref: organize randoms folder into Academic Theses and Community Board Examples`
- `repo: track images via LFS, ignore Project Outputs`

Applies going forward only — older commits predate this convention.

## 7. If something looks stuck

Locked a file but not actually editing it anymore (forgot to unlock last
time)? Just unlock it — it's a courtesy flag, not a hard restriction.

Unsure of repo state: **TortoiseGit → Show Log** (full history),
**Check for Modifications** (local vs. GitHub).

## 8. Troubleshooting

### Altium says a sheet "could not be found" / is "marked as missing"

Git LFS didn't download the real file content — you got placeholder
"pointer" text files (or empty `Sheets\` folders) instead of the real
`.SchDoc`/`.PcbDoc` files. Usually means LFS wasn't installed yet when you
cloned, or you cloned from inside Altium.

Fix — close Altium, open a terminal in the repo folder:

```
git lfs version
```

- Not recognized? Install Git LFS from https://git-lfs.com/ first.

```
git lfs install
git reset
git lfs pull
```

- `git reset` un-stages anything queued for commit (doesn't touch files on
  disk) — this situation often stages every file as **deleted**.
- `git lfs pull` replaces the placeholders with real content.

`git status` should then say `nothing to commit, working tree clean`. Reopen
the project in Altium.

> **Warning:** before every commit, check the file list. Lots of files marked
> **deleted** that you didn't delete? **Do not commit or push** — that would
> delete the project from GitHub for everyone. Run the fix above instead.

### Altium warns "LFS repository '…' is not supported"

Altium's own Git panel doesn't understand Git LFS. Harmless to ignore, but:
**don't use Altium's own Git buttons** on this repo. Use TortoiseGit or the
command line.

### A laptop holding a lock breaks/is lost

The lock lives on GitHub's servers, not on the laptop — it's just unreachable
*to release*, not unreachable *to clear*.

Only a GitHub **Admin** can force-unlock someone else's lock (not just anyone
with push access). The repo owner always has Admin.

As Admin, from any working machine:

1. `git lfs locks` — see what's locked.
2. `git lfs unlock --force "path\to\File.SchDoc"`
   (TortoiseGit: right-click the file → Unlock — Admin gets a force option.)
3. File's free, anyone can lock/edit it.

This only clears the lock flag — it doesn't recover edits that only existed
on the dead laptop and were never pushed. Anything committed and pushed is
already safe on GitHub and in other clones. Push right after you finish
editing, so the most you could ever lose is whatever you did since your last
push.
