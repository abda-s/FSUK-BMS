# Git + TortoiseGit for this repo — step by step

This is written for someone who has never used Git before. Follow it in order
the first time; after that you'll only need the "Day-to-day workflow" section.

## 1. Install the tools (once)

1. [Git for Windows](https://git-scm.com/downloads) — default options are fine.
2. [Git LFS](https://git-lfs.com/) — download, run the installer.
3. [TortoiseGit](https://tortoisegit.org/) — install, and when it asks, let it
   use the Git you just installed. Reboot if it asks you to.
   - **If the installer stops with an error about "Microsoft Visual C++
     2015-2022 Redistributable" being required:** install that first, then
     re-run the TortoiseGit installer.
     - Download: https://aka.ms/vs/17/release/vc_redist.x64.exe (this is the
       one almost everyone needs — normal 64-bit Windows).
     - Run it (Install → Close, no options to change), then retry TortoiseGit.
     - If TortoiseGit still complains after that, also install
       https://aka.ms/vs/17/release/vc_redist.x86.exe and try again.
4. Make a free [GitHub](https://github.com) account if you don't have one, and
   ask the repo owner to invite you as a collaborator on the repo.

## 2. Clone the repo (once)

Cloning = downloading your own local copy of the whole project, including its
full history.

1. Make a folder somewhere sensible, e.g. `C:\FSAE\`.
2. Right-click inside that folder → **Git Clone...**
3. Paste the repo URL (the owner will give you this — looks like
   `https://github.com/<owner>/FSUK-BMS.git`).
4. Click OK. TortoiseGit downloads everything.
5. Open a Command Prompt / PowerShell **inside the cloned folder** and run:
   ```
   git lfs install
   ```
   This is a one-time step per computer — it teaches Git on your machine how to
   handle the large Altium/PDF files properly. If you skip this, the Altium
   files you download will just be tiny placeholder text files that Altium
   can't open.
6. Still in that same window, run:
   ```
   git lfs pull
   ```
   This downloads the real Altium/PDF files. Then check that
   `BMS-Master\Sheets\` and `BMS-Module\Sheets\` actually contain `.SchDoc`
   files before you open anything in Altium.
7. Tell Git who you are (once per computer), using your GitHub username and
   the email on your GitHub account:
   ```
   git config --global user.name "your-github-username"
   git config --global user.email "you@example.com"
   ```
   This is the name that shows up on your commits.
8. Sign in to GitHub (once per computer):
   ```
   git credential-manager github login
   ```
   A browser window opens — approve it. (If you skip this, the same sign-in
   pops up automatically the first time you push.) You also need to have been
   added as a collaborator on the repo, or your pushes will be rejected.

## 3. Why you'll "lock" files before editing

The `.SchDoc`, `.PcbDoc`, `.SchLib`, and `.PcbLib` files in this repo are binary
(not text), so Git can't merge two people's changes to the same file the way it
can with code. If you and your teammate both edit `Top.SchDoc` and both push,
whoever pushes second will hit a conflict Git cannot auto-resolve, and someone
loses work.

The fix: **lock the file before you start editing it.** This tells GitHub "I'm
working on this, don't let anyone else push changes to it," and makes it
read-only on their machine until you unlock it.

## 4. Day-to-day workflow

**Before you start working, every time:**

1. Right-click the repo folder → **TortoiseGit → Pull.** Get the latest version
   of everything.

**Before you edit a specific Altium file:**

2. Right-click that specific file (e.g. `Top.SchDoc`) → **TortoiseGit → Lock.**
   - If it's already locked by someone else, TortoiseGit will tell you — message
     them, don't edit it, work on something else until they unlock it.
3. Now edit it in Altium as normal, and save.

**After you're done editing (same session, or end of day):**

4. Right-click the repo folder → **TortoiseGit → Commit...**
   - Tick the files you changed.
   - Write a short message saying what you did, e.g. `Add CAN transceiver
     circuit to CAN.SchDoc`.
   - Click Commit.
5. Right-click the repo folder → **TortoiseGit → Push.** This uploads your
   commit to GitHub so your teammate can pull it.
6. Right-click the file(s) you locked → **TortoiseGit → Unlock**, so your
   teammate can lock and edit them next.

That's the whole loop: **Pull → Lock → Edit → Commit → Push → Unlock.**

## 5. Rules of thumb

- **Never sit on a lock.** Lock right before you edit, unlock as soon as you've
  pushed. A file locked overnight for no reason just blocks your teammate.
- **`Top.SchDoc` in each project is the one everybody wants to touch.** Always
  lock it first, make your change, and push quickly — don't leave it locked
  while you go do something else.
- **Pull before every session.** If you open Altium on an old version of a file
  and edit it, you're wasting work — you'll have to redo it on top of the
  latest version anyway.
- **If a push is rejected** ("failed, non-fast-forward" or similar): someone
  pushed before you. Pull first (TortoiseGit will merge or tell you if there's
  a real conflict — for binary/locked files this should be rare if everyone
  locks properly), then push again.
- **Commit messages**: one line, plain English, say what changed — e.g.
  `Fix balancing FET footprint`, `Route power sheet`, `Add EU DoC datasheet`.

## 6. If something looks stuck

If a file shows as locked by you but you're not actually editing it anymore
(e.g. you forgot to unlock last time), just unlock it — locks are just a
courtesy flag, not a hard technical restriction, and safe to release once
you're done.

If you're ever unsure what state the repo is in, right-click → **TortoiseGit →
Show Log** shows the full history, and **Check for Modifications** shows what's
changed locally vs. what's on GitHub.

## 7. Troubleshooting

### Altium says a sheet "could not be found" / is "marked as missing"

If Altium reports errors like `Top.SchDoc could not be found... marked as
missing`, it means Git LFS didn't actually download the real file content —
you ended up with tiny placeholder "pointer" text files (or nothing at all, so
the `Sheets\` folders are empty) instead of the real binary
`.SchDoc`/`.PcbDoc` files. This usually happens if Git LFS wasn't installed
yet at the time you cloned, or the repo was cloned from inside Altium.

Fix — close Altium, open a Command Prompt / PowerShell in the repo folder, and
run:

```
git lfs version
```

- If that says the command isn't recognized, install Git LFS from
  https://git-lfs.com/ first, then continue.

```
git lfs install
git reset
git lfs pull
```

- `git reset` only un-stages anything Git has queued up for the next commit;
  it doesn't touch the files on disk. It's there because in this situation Git
  often ends up with every file staged as **deleted** (see the warning below).
- `git lfs pull` replaces the placeholder files with the real content.

Then run `git status` — it should say `nothing to commit, working tree clean`.
Close and reopen the project in Altium afterwards.

> **Warning:** before every commit, look at the list of files. If you see lots
> of files marked as **deleted** that you didn't delete, **do not commit or
> push** — that would delete the whole project from GitHub for everyone. Run
> the fix above instead.

### Altium warns "LFS repository '…' is not supported"

Altium has its own built-in Git panel, and it doesn't understand Git LFS.
The warning itself is harmless and can be ignored, but it means: **don't use
Altium's own Git buttons** (commit / update / clone) on this repo. Always use
TortoiseGit or the command line, which handle LFS properly.

### A laptop holding a lock breaks/is lost — how do we get the file back?

The lock is **not** stored on that laptop — it's a record on GitHub's servers,
tied to the person's account. The laptop breaking doesn't trap the lock
anywhere unreachable; it just means that person can't be the one to release it
themselves.

Only a GitHub **Admin** on the repo can force-unlock someone else's lock (not
just anyone with push access). The repo owner always has Admin, so they can
always do this even if nobody else can.

As the Admin, from any working machine:

1. See what's locked: `git lfs locks`
2. Force it open: `git lfs unlock --force "path\to\File.SchDoc"`
   (In TortoiseGit: right-click the file → Unlock. Since you're Admin, it'll
   let you force-unlock a lock someone else holds.)
3. The file is free — anyone can lock and edit it normally now.

**This only clears the lock flag.** It does not recover any edits that only
existed on the dead laptop and were never pushed — that work is genuinely
gone, the same way it would be with or without locking. Anything that *was*
committed and pushed is already safe, sitting on GitHub and in the other
person's local clone. This is exactly why the day-to-day workflow says not to
sit on a lock: push right after you finish editing, and the most you could
ever lose to a dead laptop is whatever you did since your last push.
