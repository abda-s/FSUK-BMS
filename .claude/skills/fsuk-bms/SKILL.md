---
name: fsuk-bms
description: How to work on the FSUK-BMS repo (Formula Student accumulator BMS, Altium + STM32). Use for any schematic/Altium change, part import, datasheet check, LTspice sim, firmware/CubeMX work, README update or commit in this project.
---

# FSUK-BMS

## User rules
- Plain factual writing, no hype ("don't larp"), keep all info. Cite sources (datasheet section/table/figure, URLs, rule numbers).
- Research/read the datasheet before acting or answering; say what was checked and what wasn't.
- Commit/push only when asked. Never put the SDC TDR file in the repo. Never type credentials. No proxy/IP rotation for EasyEDA.
- Altium: place/import parts freely; wire only when asked. The user edits the same sheet while Claude works: re-read positions right before every change.
- When the user says stop, stop and wait. Keep messages short; tell the user about anything that failed or was routed around.
- Use smaller models (haiku/sonnet subagents) for easy, mechanical work (doc edits, file sorting, simple lookups); keep design decisions and Altium scripting in the main session.

## Repo map (E:\Documents\Racing\FSUK-BMS, GitHub abda-s/FSUK-BMS, branch main)
- `BMS-Master/` Altium project (`BMS-Master.PrjPcb`, `Sheets/*.SchDoc`), `README.md` (design write-up, Progress/to-do at the end), `docs/sch/*.png`, `docs/power/`, `sim/buck/` (LTspice), `BMS-Master_Schematics.pdf` (user exports via `BMS-Master.OutJob`).
- `BMS-Module/` second Altium project. `Firmware/BMS-Master/` CubeMX/CubeIDE project (STM32G474RET6), `Firmware/README.md` (pin table, settings).
- `Reference Docs/` (Shared/Master/Module + reading guide). Markdown versions of every PDF in `Reference Docs/MD Conversions/<same path>/`; read those first.
- `tools/pdf2md.py` (PDF to Markdown, GPU), `tools/emf2png.ps1` (schematic image capture).

## Where to look
- Altium scripting patterns, part import, schematic images: `references/altium.md`.
- Every Altium script failure so far (read before writing a script, append after a new failure): `references/script-errors.md`.
- Design decisions, pin map, part numbers, open items: `references/design.md`.
- LTspice, CubeMX/CubeIDE, pdf2md/GPU, the OCR book project, git: `references/tools.md`.

## Workflow
1. Before an Altium script: read `references/script-errors.md` and the API reference for anything new. Read-only check first, then modify, save, compile, and quote the resulting nets.
2. Before bulk moves/renames: dump pin->net to a file, change, dump again, `diff` (must be identical).
3. After a schematic change the README shows: recapture its image (no notes), update the section text with datasheet references, update Progress (Done one-liners, new to-dos). Check to-dos against the actual sheets before ticking.
4. Datasheet questions: open the `.md` in `MD Conversions`, then a rendered page (pymupdf) for merged-cell tables or figures.
5. Commit when asked: `git status`, check nothing sensitive/build output, one clear message ending with the Co-Authored-By line, push.
