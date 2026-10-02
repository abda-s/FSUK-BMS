# FSUK-BMS

Battery Management System hardware for the FSUK electric accumulator: a 16-series
cell-monitor module (`BMS-Module`, built with the TI BQ79616) daisy-chained back
to a central controller board (`BMS-Master`, built with the TI BQ79600-Q1 bridge
and an STM32 MCU that talks CAN to the car's ECU).

## Repo layout

```
FSUK-BMS/
├── BMS-Master/       Altium project — controller board (STM32, BQ79600-Q1, CAN)
├── BMS-Module/       Altium project — cell-monitor board (BQ79616), built x6
└── Reference Docs/   Datasheets, app notes, and the TIDA-010271 reference design
```

`BMS-Master` and `BMS-Module` are two **separate, standalone Altium projects** —
open each one on its own (no shared workspace file). They're separate boards with
separate BOMs and separate release cycles, so this keeps things simple.

**Design documentation lives in each board's own `README.md`**
(`BMS-Master/README.md`, `BMS-Module/README.md`) — block diagram and a `##`
section per major design decision (MCU selection, etc.). Add new decisions as
a new section there rather than a new standalone file, so each board has one
place anyone can land on and read top to bottom.

## One-time setup (do this before opening anything in Altium)

1. Install [Git](https://git-scm.com/downloads).
2. Install [Git LFS](https://git-lfs.com/) — this repo stores all the Altium
   design files (`.SchDoc`, `.PcbDoc`, `.SchLib`, `.PcbLib`) and PDFs through it,
   because they're binary files and regular git handles those very badly.
3. Install [TortoiseGit](https://tortoisegit.org/) — gives you Git through
   right-click menus in File Explorer, no command line needed.
4. Clone this repo (see below), then in the cloned folder run once:
   ```
   git lfs install
   git lfs pull
   ```
   Check that the `Sheets\` folders contain `.SchDoc` files before opening
   Altium. If Altium says sheets are "missing", see **Troubleshooting** in
   `Docs/GIT_FOR_ALTIUM.md`.
5. Set your Git name/email and sign in to GitHub — see step 2 of
   `Docs/GIT_FOR_ALTIUM.md`.

Use TortoiseGit or the command line for all Git operations — **not** Altium's
built-in Git support, which doesn't handle Git LFS.

## Why Git LFS + file locking (read this before editing anything)

Altium files (`.SchDoc`, `.PcbDoc`, `.SchLib`, `.PcbLib`) are **binary** — unlike
code, Git cannot merge two people's edits to the same file. If you and a
teammate both edit `Top.SchDoc` at the same time and both push, one of you will
have to throw away your changes and redo them.

To prevent that, these file types are set up as **"lockable"** in this repo.
Before editing one of them, you lock it — this reserves it for you and makes it
read-only for everyone else until you unlock it. See the workflow section below.

## Day-to-day workflow

1. **Pull** the latest changes before you start working.
2. **Lock** the specific file(s) you're about to edit.
3. Edit in Altium, save.
4. **Run the project's Output Job** (`BMS-Master.OutJob` / `BMS-Module.OutJob`,
   visible in the Projects panel) to regenerate the schematic PDF — right-click
   it → **Run**. First time you run it, Altium may ask where to save the PDF;
   point it at a `Project Outputs` folder inside the project (already
   git-ignored) and it'll remember that choice afterwards.
5. **Commit** with a short message describing what changed (include the
   regenerated PDF in the commit).
6. **Push.**
7. **Unlock** the file(s) so someone else can edit them next.

The Output Job means anyone can open the latest schematic PDF straight from
GitHub without needing Altium installed — handy for reviewing on a phone/
laptop that doesn't have it.

See `Docs/GIT_FOR_ALTIUM.md` for the exact TortoiseGit click-by-click steps.
