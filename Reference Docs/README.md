# Reference Docs

Datasheets, app notes, rules and other teams' work used for the BMS design.

```
Reference Docs/
├── Shared/   Used by both boards: daisy chain, isolation, rules, other teams' designs
├── Master/   BMS-Master parts: BQ79600, STM32, CAN, current sensor, power, charger, AMS_OK
└── Module/   BMS-Module parts: BQ79616, TIDA-010271 reference design
```

## Where to start

If you're new, read these in order. Steps 1–5 are enough to follow the
schematics; 6 is for firmware.

1. **What the system looks like:**
   [`Shared/BQ796xx/Scaling Battery Management Designs - App Brief (slvafq7).pdf`](Shared/BQ796xx/)
   (2 pages). Shows BQ79616 monitors daisy-chained to a controller with a
   BQ79600 bridge, which is our architecture.
2. **The two TI chips.** In each datasheet read the first page (Features,
   Description) and the Overview and Functional Block Diagram at the start of
   Detailed Description. Skip the register map for now.
   - [`Module/BQ79616/BQ79616 16-Cell Battery Monitor Datasheet (bq79616).pdf`](Module/BQ79616/):
     the cell monitor on every module (16 cells, temperatures, balancing).
   - [`Master/BQ79600/BQ79600-Q1 Comms Bridge Datasheet (bq79600-q1).pdf`](Master/BQ79600/):
     the bridge on the master, between the MCU (SPI/UART) and the daisy chain.
3. **How the chips talk:**
   [`Shared/BQ796xx/BQ79616-Q1 Daisy Chain Communications (slvaep4).pdf`](Shared/BQ796xx/).
   The daisy-chain protocol (frames, timing) and isolation with transformers
   or capacitors.
4. **What the schematics must include** (TI's design recommendations):
   - Module: [`Module/BQ79616/BQ7961x-Q1 High Voltage BMS Design Recommendations (slvae87b).pdf`](Module/BQ79616/)
   - Master: [`Master/BQ79600/BQ79600-Q1 Design Recommendations (sluaa16a).pdf`](Master/BQ79600/):
     power pins, layout, daisy-chain signal integrity.
5. **A complete design:**
   [`Module/TIDA-010271 Reference Design/`](Module/TIDA-010271%20Reference%20Design/).
   TI's stackable battery-monitor board (32S, two BQ79616), daisy chain with
   ring support. Read the Design Guide (tiduf46) first, then the Schematic
   (tidmc03) and PCB Layout (tidmc06). The Altium source is in the `tidmc07`
   folder.
6. **Firmware / bring-up:**
   - [`Master/BQ79600/BQ79600-Q1 Bring-Up Procedure (sluuc56c).pdf`](Master/BQ79600/):
     the three steps to start the stack: device setup, wakeup, auto-addressing.
   - `BQ79600-Q1 Software Design Reference (sluaa17a)` and
     `BQ79616-Q1 Software Design Reference (slvae86b)`: command frames
     (single/stack/broadcast read and write) with example bytes.

Then the rules: [`Shared/FSUK Rules/`](Shared/FSUK%20Rules/) (FSG 2026 v1.1 and
the FSUK 2026 supplementary). The ones our design is checked against are
listed in each section of [`BMS-Master/README.md`](../BMS-Master/README.md)
(e.g. EV 1.2.1 isolation, EV 4.3.5 TS/LV segregation, T 11.9).

## Shared

| Folder | Contents |
|---|---|
| `BQ796xx/` | Daisy-chain app note, scaling app brief, MSPM0 UART-to-CAN example, reverse-wakeup and energy-storage articles, BQ79631/BQ79731 functional-safety whitepaper |
| `BMS Isolation Transformers/` | Daisy-chain transformers compared for the master and modules (SM91502AL chosen, HMU1228NL, Pulse BM101, CND-tek CB0603S) |
| `Common Mode Chokes/` | Chokes considered for the daisy chain |
| `ESD Protection/` | ESD diodes considered |
| `FSUK Rules/` | FSG 2026 v1.1 rules, FSUK 2026 supplementary |
| `Academic Theses and Reports/` | Formula Student BMS theses and design reports from other universities |
| `Community Board Examples/` | Other teams' schematics and boards (BMS master, precharge, TSAL) |
| `Open-Source BMS Projects/` | Open-source BMS repos. Not in git (licences, size); its README lists them and how to clone |
| `links.md` | Web links found during research |

## Master

Used by [`BMS-Master/README.md`](../BMS-Master/README.md); each section there
says which file it comes from.

| Folder | Contents |
|---|---|
| `BQ79600/` | BQ79600-Q1 datasheet, design recommendations, software reference, bring-up procedure |
| `STM32 MCU/` | STM32G474 datasheet (DS12288) |
| `CAN Transceivers/` | TCAN1042-Q1 (used), TCAN1462-Q1, TJA1057, MCP2561/2FD |
| `Current Sensor/` | LEM DHAB S/124 (used) and the alternatives compared |
| `TS Cable/` | TS cable datasheet (current-sensor insulation argument) |
| `Power/` | TPS62933F buck datasheet, PSpice model, WEBENCH design, LMR51430, SMBJ16A TVS |
| `LDO/` | TLV761 (used) and the other LDOs compared |
| `AMS_OK Driver/` | MOSFETs and relays for the `AMS_OK` output |
| `Optocouplers/` | PC817 (charger stop signal) |
| `Manzanita PFC-20 Charger/` | Charger datasheet and manual (Reg Bus wiring) |
| `Balancing Switch/` | ALPS SSSS811101 (balancing master switch) |
| `Watchdog/` | TPS3431 (planned for v2) |

## Module

| Folder | Contents |
|---|---|
| `BQ79616/` | BQ79616 datasheet, HV BMS design recommendations, software reference, EVM and GUI user guides, EVM declaration of conformity, autonomous cell balancing article |
| `TIDA-010271 Reference Design/` | TI reference design: design guide, schematic, BOM, PCB layout, assembly drawing, Altium source |
