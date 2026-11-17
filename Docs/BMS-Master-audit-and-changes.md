# BMS-Master — audit, parts re-import, crystal swap, test points

Session log for the BMS-Master schematic work (Nov 2026). Covers what was
checked, what changed, and why. Commits are on `main`.

## Summary

| Area | What changed |
|---|---|
| **Parts** | 42 generic "Celestial" passives re-imported as EasyEDA/LCSC parts (every R/C now has an LCSC code) |
| **Crystal** | HC-49S through-hole → SCTF SX5A20.000F2010F30G 5032 SMD (C5830635), load caps 22 pF → 12 pF C0G |
| **Test points** | 20 added (Keystone 5015, C2906768) across power, BQ SPI, sense, AMS_OK, CAN |
| **COML** | R29 (1 kΩ termination) removed — COMLP/COMLN left unconnected |
| **Docs** | Crystal datasheet installed; README updated (crystal section, Q1/Q2, net names, test points) |
| **Tooling** | `tools/schdump.py`, `schnetlist.py`, `netcmp.py`, `bomcheck.py`, `stockcheck.py` |

## 1. Schematic audit

The Altium MCP server wasn't attached to the session at first, so the audit was
done by parsing the `.SchDoc` files directly (OLE `FileHeader` stream) and
rebuilding the netlist from wire/pin/label geometry. Findings:

- **42 of 108 parts were generic `Capacitor`/`Resistor` symbols from the
  Celestial library with no LCSC number** (the rest were EasyEDA imports).
- Crystal (X1) was the HC-49S through-hole `X49SD20MSD2SC` (C16370):
  20 MHz, CL 20 pF, ESR 45 Ω, ±20 ppm, −20…+70 °C — electrically marginal for
  the STM32G474 and the wrong package.
- Net-name / doc drift: net is `+6V94` (README said `+6V5`); Q1/Q2 roles and
  LCSC numbers were swapped in the README; the schematic held 108 parts (not 123).
- `COMLP`/`COMLN` were tied with a 1 kΩ resistor although the port is unused
  (TI SLUAA16A §1.5: "leave unconnected if not used").

## 2. Crystal selection and swap

- **Hard limit check (AN2867 Rev 23):** `gmcrit = 4·ESR·(2πF)²·(C0+CL)²`, must
  be below the STM32G474 HSE `Gm = 1.5 mA/V` (DS12288 Table 41).
  - Old HC-49S (45 Ω, 20 pF): gmcrit ≈ 2.07 mA/V → **fails**.
  - New SCTF SX5A20 (40 Ω, 10 pF, C0 5 pF): gmcrit ≈ 0.57 mA/V → **2.6× margin, passes**.
- **Chosen: SCTF SX5A20.000F2010F30G (LCSC C5830635)**, 5032 2-pad SMD,
  20 MHz, CL 10 pF, ESR 40 Ω, ±20 ppm, −40…+85 °C.
  - C5830634 (±10 ppm) was the first pick but has no EasyEDA model, so its
    identical-footprint sibling C5830635 is used.
- **Load caps:** C13/C14 22 pF → **12 pF C0G** (`CL05C120JB5NNNC`, C26406)
  (CL = 10 pF, C = 2·(10 − 4 pF stray) = 12 pF).
- The crystal note on `MCU_STM32.SchDoc` was updated (10 pF → 12 pF).
- Datasheet installed at `Reference Docs/Master/Crystal/SCTF SX5A Crystal Datasheet.pdf`
  (+ Markdown conversion).

## 3. Passive re-import (42 parts)

The 42 Celestial passives were replaced in place with EasyEDA-plugin imports
(batch import → move onto the old location → delete old → renumber), reusing
LCSC codes already in the project where possible:

| Value | LCSC | MPN |
|---|---|---|
| 100 nF 0402 | C1525 | CL05B104KO5NNNC |
| 100 nF 0603 | C14663 | CC0603KRX7R9BB104 |
| 4.7 µF 0603 | C77045 | GRM188R61C475KE11D |
| 1 µF 0603 | C113807 | CC0603KRX7R6BB105 |
| 22 pF (now 12 pF) | C70464 → C26406 | CL05C120JB5NNNC |
| 20 pF 0402 C0G | C1554 | 0402CG200J500NT |
| 0.22 µF 0603 | C64705 | CL10B224KB8NNNC |
| 10 nF 0402 | C318577 | CL05B103KO5NNNC |
| 100 pF 0402 C0G | C26409 | CL05C101JB5NNNC |
| 10 kΩ 0402 | C2906861 | FRC0402F1002TS |
| 100 kΩ 0402 | C25530 | 0402WGJ0104TCE |
| 0 Ω 0402 | C17168 | 0402WGF0000TCE |
| 1 kΩ 0402 | C11702 | 0402WGF1001TCE |
| 500 Ω 0402 | C6460545 | RT0402FRE07500RL |
| 49.9 Ω 1206 | C18018 | 1206W4F499JT5E |

Connectivity was verified per sheet (per-designator net sets identical before
and after). Every component now carries an LCSC `Supplier Part`.

## 4. Test points (20)

Keystone **5015** (C2906768), single-pin SMD loop, one 3.43 × 1.78 mm pad
(footprint `TEST-SMD_L2.7-W1.0`). Each is a short stub + net label.

| Sheet | Designators | Nets |
|---|---|---|
| Power | TP1–TP5 | +12V, +6V94, +5V, +3V3, GND |
| MCU_STM32 | TP6–TP15 | BQ_SCLK, BQ_MOSI, BQ_MISO, BQ_nCS, BQ_NFAULT, BQ_SPI_RDY, MCU_NRST, BAL_EN_N, CHG_EN, GND |
| Current_Sense | TP16, TP17 | ISENSE_HI, ISENSE_LO |
| AMS_SDC | TP18 | AMS_OK |
| CAN (→ CAN1, CAN2) | TP19, TP20 | CAN_P, CAN_N |

Deliberately skipped: crystal nets (a probe loads the oscillator), the daisy
chain / ISO_COMH (TS side, reachable at J2), the charger Reg Bus (mains
potential), SWD (already on J4).

## 5. Other design notes

- **T1 pin 5 (secondary centre-tap) is intentionally floating.** The
  SM91502ALE is the TS/LV barrier; pin 2 (primary CT) is AC-coupled to GND via
  100 pF (correct, LV side), but pin 5 (secondary CT) must **not** go to LV GND
  — that would put a capacitor across the barrier and fail EV 1.2.1 (1209 Vrms)
  / break EV 4.3.1 galvanic isolation. The first module's transformer sets the
  pair's common mode.
- **R29 removed** (by the user): COMLP/COMLN now unconnected, matching TI.

## 6. Tooling (`tools/`)

- `schdump.py` — parse a `.SchDoc` (OLE) to components/pins without Altium.
- `schnetlist.py` — rebuild the netlist from wire/pin/label geometry.
- `netcmp.py` — compare two netlists per designator (ignores pin numbers).
- `bomcheck.py` — BOM analysis (per-LCSC usage, consolidation, no-LCSC, dupes).
- `stockcheck.py` — query JLCPCB/LCSC stock for every BOM part.

## 7. Stock check (60 parts)

Only one LOW: **TCAN1042VDQ1 (C1544495) at 26** (used ×2). Everything else is
healthy (STM32G474 360, BQ79600 563, crystal C5830635 245, 5015 test points 67 k).

## 8. Commits

- `cffd3d9` — "sch(master): re-import 42 Celestial passives as EasyEDA LCSC parts"
- `547a431` — "sch(master): SMD crystal + test points; R29 removed; BOM/stock tooling"
  (16 files: 6 SchDoc, README, 2 images, crystal datasheet, 5 tool scripts, skill update)

## 9. Still open

- Re-run the ERC compile and glance at the Messages panel (couldn't read the
  violation count programmatically).
- Confirm the Keystone 5015 land pattern against the datasheet (single pad vs
  Keystone's 2-pad recommendation) — electrically fine either way.
- Watch TCAN1042VDQ1 stock; check SOIC-8 TCAN1462VDRQ1 before v2.
- COML (ring) second connector, external watchdog, SDC readback, heartbeat
  AMS_OK — unchanged v2 items in the README to-do list.
