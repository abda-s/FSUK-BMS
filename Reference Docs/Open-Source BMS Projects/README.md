# Open-Source BMS Projects (reference only — not tracked in this repo)

These are other teams'/projects' full BMS repositories, cloned here for
studying their schematics/PCB/firmware approach. They are **not committed to
our git history** — several are 150MB-1GB+ and most carry no license, so we
have no right to redistribute their source under our own repo. Clone them
locally with the commands below whenever you want them.

Entries marked **no license** = all rights reserved by default — read and
learn from them, don't copy their code/schematics directly. Entries marked
with a license name are actually safe to reuse/adapt under that license's
terms (credit the author, and for copyleft licenses like GPL keep derivative
work under the same license).

## Automotive / Formula Student relevant

- **FSAE_LSU_BMS** — LSU's FSAE team. Distributed BMS built around an STM32
  MCU paired with the **BQ79616/BQ79614/BQ79612** family — the same TI AFE chip
  family we're using. Most directly comparable project we've found.
  *No license.*
  ```
  git clone https://github.com/JacobParent7/FSAE_LSU_BMS.git
  ```
- **g474-bms** — University of Manchester's FSAE team (Manchester Stinger
  Motorsports). Confirms a real FS team using the **STM32G474RET6** — a chip
  we considered for `BMS-Master`. Uses an ADBMS6822 AFE (different from our
  BQ79616, but the MCU choice/peripheral usage is directly relevant).
  *No license.*
  ```
  git clone https://github.com/ManchesterStingerMotorsports/g474-bms.git
  ```
- **Battery-Management-System-LTC6811-STM32** — a full master+slave BMS built
  around the LTC6811 AFE + STM32F446RE, with real Altium schematic sheets that
  map closely onto our own sheet split (Microcontroller, CAN, CellCircuit,
  BatteryStackMonitor, Thermistors). Large (~1GB, mostly fabrication outputs).
  **MIT licensed** — safe to reuse with credit.
  ```
  git clone https://github.com/vamoirid/Battery-Management-System-LTC6811-STM32.git
  ```
- **EV-BMS-Cell-Protection** — small, focused Formula Student board: an
  overvoltage/undervoltage window-comparator protection circuit for a single
  cell. Good narrow reference for analog cell-protection circuitry.
  **MIT licensed** — safe to reuse with credit.
  ```
  git clone https://github.com/jimchantes/EV-BMS-Cell-Protection.git
  ```

## General / non-automotive open-source BMS (still useful design references)

- **OpenBMS** — scalable daisy-chain BMS (KiCad), stackable Major/Micro Master
  modules + cell-manager (slave) boards, up to 96 cells / 400V+ across
  multiple revisions. Good master+slave daisy-chain architecture reference,
  same general topology as our `BMS-Master`/`BMS-Module` split.
  *No license.*
  ```
  git clone https://github.com/igeeks/OpenBMS.git
  ```
- **evoone-bms-pcb** — single-board KiCad BMS (EvoOne), multiple schematic
  sheets (input protection, battery management, step-up/down regulation,
  load switch + current sense).
  *No license.*
  ```
  git clone https://github.com/evosonic/evoone-bms-pcb.git
  ```
- **evBMS** — small master + slave pair (`MMMaster` + `6802Slave`) built
  around the older LTC6802 AFE. Minimal/early-stage but a real second example
  of a distributed master/slave split.
  **TAPR Open Hardware License** — an open-hardware-specific license, check its
  terms before reusing directly.
  ```
  git clone https://github.com/Greg-Fordyce/evBMS.git
  ```
- **BMS-Can-Bus** — compact single-board KiCad design, **BQ76952** (same TI
  battery-monitor product line as our BQ79616, smaller/non-automotive variant)
  + CAN bus output.
  **MIT licensed** — safe to reuse with credit.
  ```
  git clone https://github.com/hasanberkdasar/BMS-Can-Bus.git
  ```

## One-time setup if you don't have these yet

Run the `git clone` commands above from inside this folder
(`Reference Docs/Open-Source BMS Projects/`). They won't show up as changes
in `git status` — they're gitignored on purpose.

## Note

A seventh candidate, `ljordan51/PCBs` (Olin College's FSAE team — precharge/AIL,
master switch panel monitor, and TSAL boards), only contained exported
PDFs/STEP files, not editable source — so instead of cloning the whole repo,
the relevant exports were copied directly into
`Reference Docs/Community Board Examples/`.
