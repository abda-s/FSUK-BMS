# Open-Source BMS Projects (reference only — not tracked in this repo)

These are other teams' full BMS repositories, cloned here for studying their
schematics/firmware approach. They are **not committed to our git history** —
each one is 16-220MB and (except ENNOID-BMS) carries no license, so we have
no right to redistribute their source under our own repo. Clone them locally
with the commands below whenever you want them.

## What's here

- **FSAE_LSU_BMS** — LSU's FSAE team. Distributed BMS built around an STM32 MCU
  paired with the **BQ79616/BQ79614/BQ79612** family — the same TI AFE chip
  family we're using. Most directly comparable project we've found.
  No license file (all rights reserved) — read for ideas, don't copy code.
  ```
  git clone https://github.com/JacobParent7/FSAE_LSU_BMS.git
  ```
- **g474-bms** — University of Manchester's FSAE team (Manchester Stinger
  Motorsports). Confirms a real FS team using the **STM32G474RET6** — the exact
  chip we're considering for `BMS-Master`. Uses an ADBMS6822 AFE (different
  from our BQ79616, but the MCU choice/peripheral usage is directly relevant).
  No license file (all rights reserved) — read for ideas, don't copy code.
  ```
  git clone https://github.com/ManchesterStingerMotorsports/g474-bms.git
  ```
- **ENNOID-BMS** — open-source modular BMS for up to 400V EV packs, built on
  LTC68XX AFE chips + STM32. **Licensed GPLv3** — actually fine to reuse/adapt
  code from, as long as anything we build on it also stays GPLv3 and credits
  them.
  ```
  git clone https://github.com/EnnoidMe/ENNOID-BMS.git
  ```

## One-time setup if you don't have these yet

Run the three `git clone` commands above from inside this folder
(`Reference Docs/Open-Source BMS Projects/`). They won't show up as changes
in `git status` — they're gitignored on purpose.
