# BMS-Master

Controller board for the FSUK accumulator: bridges to the daisy-chained
cell-monitor stack (`BMS-Module`, x6) via a BQ79600-Q1, runs the safety logic
(limit checks, SoC estimation, balancing control, fault latch), and talks two
CAN buses — full telemetry, and a summarized feed to the ECU/dashboard.

This file is the design-documentation hub for this board — add a new `##`
section here for each major design decision rather than creating a new
standalone file per topic.

## Block diagram

![BMS-Master Block Diagram](block-diagram.png)

- Talks to the **BQ79600-Q1 bridge** over SPI (plus `SPI_RDY` and `NFAULT`
  interrupt lines) to read the whole daisy-chained cell-monitor stack.
- Reads the **accumulator current sensor**.
- Runs **cell/temperature limit checks, SoC estimation, balancing control,
  and the fault latch** — the actual safety logic.
- Drives the **AMS fault relay** — a single signal that opens the shutdown
  circuit (SDC) directly, not routed through the ECU over CAN. Must work
  correctly whether the car is driving or charging.
- Talks **two separate CAN buses**: CAN1 (full telemetry — all 96 cells, 192
  temperatures, balancing state, current, voltage) and CAN2 (summarized
  state — SoC, max cell voltage, max temperature, fault code — to the ECU/
  dashboard).
- Drives the **isolated charger regulation bus** (opto-isolated STOP signal).
- Is watched by an **external watchdog** that opens the relay if the MCU
  hangs.

## MCU selection: STM32G474

**STM32G474** (fallback: **STM32G473**, pin/feature-compatible — use only if
G474 is out of stock).

It's the only candidate that passes every "Must" requirement *and* leads on
every "Nice to have" — built-in op-amps/PGAs, the most ADCs, and 3x FDCAN
peripherals with room to spare. Several other candidates also pass all
must-haves (see the full matrix below), but none of them beat G474 on
anything — they're sideways-or-worse choices, not real alternatives.

### Requirements and why they matter

| # | Requirement | Priority | Why |
|---|---|---|---|
| 1 | At least 2 CAN peripherals | **Must** | CAN1 for full telemetry/diagnostics, CAN2 for ECU/dashboard. Classic CAN or CAN-FD both count. |
| 2 | CAN FD support | Nice | Bonus only — a 64 B CAN-FD frame needs ~7 frames per snapshot vs ~55 on classic CAN, but classic CAN at 1 Mbps already does a full snapshot in ~7 ms. Not a deciding factor. |
| 3 | SPI master for the BQ79600-Q1 bridge | **Must** | At least one SPI peripheral, plus the `SPI_RDY` and `NFAULT` interrupt pins. |
| 4 | Hardware FPU | **Must** | For SoC estimation algorithms. |
| 5 | RAM / Flash capacity | **Must** | A snapshot is only ~420 B, but there's also limit tables, balancing state, the fault latch, and CAN queues to hold. |
| 6 | Fast multi-channel ADC | **Must** | Samples the accumulator current sensor. |
| 7 | Internal PGA / op-amp | Nice | Only useful if we end up using a raw analog shunt amp for current sense. A CAN-based or isolated Hall sensor makes this moot — so it's a bonus, not a blocker. |
| 8 | GPIO: 2 EXTI inputs + relay, watchdog, opto outputs, switch input | **Must** | Specifically: `SPI_RDY`, `NFAULT`, AMS relay, watchdog toggle, charger opto, balancing switch. |
| 9 | Deep CAN buffering (non-blocking TX) | Should | Telemetry must never block the safety path (AMS relay, fault latch, watchdog). |

### Candidates evaluated

STM32G474, STM32G473, STM32G491, STM32G431, STM32H503, STM32H523/H563,
STM32H723/H743, STM32F446, STM32F405, STM32F413, STM32F429/F407, STM32G0B1,
STM32F303 — a spread across ST's current CAN-capable families (G4, H5, H7,
F4, G0) plus F3 as a real-world precedent (ENNOID-BMS uses an F303 — see
`Reference Docs/Open-Source BMS Projects/README.md`).

### Comparison matrix

| Requirement | Priority | G474 | G473 | G491 | G431 | H503 | H523/H563 | H723/H743 | F446 | F405 | F413 | F429/F407 | G0B1 | F303 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ≥2 CAN peripherals | Must | Meets | Meets | Meets | **Fails** | Verify | Meets | Meets | Meets | Meets | Meets | Meets | Meets | **Fails** |
| CAN FD support | Nice | Meets | Meets | Meets | Partial | Verify | Meets | Meets | Partial | Partial | Partial | Partial | Meets | Fails |
| SPI master for BQ79600-Q1 | Must | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets |
| Hardware FPU | Must | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | **Fails** | Meets |
| RAM / Flash capacity | Must | Meets | Meets | Meets | Partial | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets |
| Fast multi-channel ADC | Must | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Partial | Meets |
| Internal PGA / op-amp | Nice | **Meets** | Meets | Partial | Meets | Fails | Fails | Fails | Fails | Fails | Fails | Fails | Fails | Verify |
| GPIO requirements | Must | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Meets |
| Deep CAN buffering | Should | Meets | Meets | Meets | Meets | Meets | Meets | Meets | Partial | Partial | Partial | Partial | Meets | Partial |

> Specs are from memory at the time of writing — **verify CAN counts, ADC
> counts, and memory sizes in CubeMX or the datasheet before committing to
> silicon.** The "Verify" cells above (H503's CAN count in particular) are
> known open questions.

### Verdict summary

| Variant | Must-haves met (of 6) | Should/Nice met (of 3) | Result | One-line verdict |
|---|---|---|---|---|
| **STM32G474** | 6/6 | 3/3 | Passes all must-haves | **Best fit. Recommended.** |
| STM32G473 | 6/6 | 3/3 | Passes all must-haves | Same as G474. Use if G474 is out of stock. |
| STM32G491 | 6/6 | 2/3 | Passes all must-haves | Fine with an external current sensor. |
| STM32G431 | 4/6 | 2/3 | **Fails a must-have** | Fails: only one CAN. |
| STM32H503 | 5/6 | 1/3 | **Fails a must-have** | Check CAN count first. |
| STM32H523/H563 | 6/6 | 2/3 | Passes all must-haves | Works. Only worth it for a faster core or secure boot. |
| STM32H723/H743 | 6/6 | 2/3 | Passes all must-haves | Overkill, big packages. |
| STM32F446 | 6/6 | 0/3 | Passes all must-haves | Best F4 choice. Classic CAN is enough. |
| STM32F405 | 6/6 | 0/3 | Passes all must-haves | Works. |
| STM32F413 | 6/6 | 0/3 | Passes all must-haves | Works, 3x CAN. |
| STM32F429/F407 | 6/6 | 0/3 | Passes all must-haves | Works, oversized. |
| STM32G0B1 | 4/6 | 2/3 | **Fails a must-have** | No FPU. Minimal-cost option only. |
| STM32F303 | 5/6 | 0/3 | **Fails a must-have** | Out: only one CAN, and it's shared with USB packet SRAM. |

### Why G474 specifically, not just "any passing candidate"

Six candidates pass every must-have (G474, G473, H523/H563, H723/H743, F446,
F405, F413, F429/F407). Among those, G474 wins because it's the only one that
also meets the internal PGA/op-amp requirement fully (the F4 family and H5/H7
family all fail it outright — no built-in op-amps at all, meaning an external
amplifier chip would be required if we ever need a raw analog shunt). It also
has the deepest CAN buffering (FDCAN message RAM vs. the F4 family's 3 TX
mailboxes, which would need an interrupt-driven software TX queue to avoid
blocking the safety path) and the most ADCs of any candidate. The H7 and large
F4 parts (F429/F407, F413) pass everything too but are bigger/pricier than
this board needs for no actual benefit here.

**G473** is functionally identical to G474 (same analog block, same CAN
count) — it's listed purely as a drop-in fallback if G474 specifically is
out of stock.

### Package note

G474 in an **LQFP64** package has enough pins for everything in the block
diagram with spare pins left over for SWD/debug.

### Sources

- Full requirements matrix, per-cell notes, and rationale:
  [Google Sheet — stm32_requirements_matrix](https://docs.google.com/spreadsheets/d/1AgWugIduUw6VQksLgAckyC9UT4bKEkQZ88cZwor0tiw/edit?usp=sharing)
- BQ79600-Q1 datasheet and app notes: `Reference Docs/BQ796xx BMS/`
- Real-world FSAE/BMS precedent for STM32 MCU choices:
  `Reference Docs/Open-Source BMS Projects/README.md`
