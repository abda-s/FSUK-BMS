# Buck converter start-up charts

Charts generated from the LTspice transient run **`../buck_startup.raw`**
(schematic `../buck_startup.asc`). Nothing in the simulation folder was modified.

Open **`index.html`** for a gallery of every chart.
Every chart exists in both **`.png`** (raster preview) and **`.svg`** (vector, real
selectable text - recommended for reports and printing).

## Circuit under test
TPS62933F buck converter, 12 V battery rail -> regulated 6.52 V into a 6.5 ohm load (1 A).
`.tran 0 9m 0 20n`, Gear integration, 2,497,138 stored points.

## Charts
| file | content |
|---|---|
| `01_startup_overview` | V(vin), V(vout), V(ss), V(en) over the full 9 ms, with t_on / t_90 markers |
| `02_output_voltage` | V(vout) ramp-up + steady-state ripple zoom (8.5-9.0 ms) |
| `03_inductor_current` | I(L1) inrush peak + steady-state ripple zoom |
| `04_switch_node` | V(sw) switching waveform (~496 kHz) with V(vout) overlaid |
| `05_power_efficiency` | P(in), P(out) and efficiency vs. time |
| `06_input_stage` | V(vin) battery/harness rail and input current I(Rh) |
| `07_control_signals` | V(en), V(ss), V(fb), V(bst) |
| `08_startup_detail` | 0 - 1.5 ms close-up of rails and currents |
| `09_summary_dashboard` | six-panel summary of every captured waveform |
| `buck_startup_data.csv` | 30 000-row decimated export of all traces + derived P/pin/eff |
| `make_charts.py` | regenerates every chart (PNG + SVG) and runs the in-figure layout check |
| `verify_svg_layout.py` | independent SVG-level overlap / clipping checker |

## Measured results (steady state, 8 - 9 ms)

| quantity | value | LTspice `.log` cross-check |
|---|---|---|
| t_on (Vout = 0.1 V) | 0.6798 ms | 100.0000 ms |
| V(vin) at t_on | 8.0699 V | 8.0695 V |
| t_90 (Vout = 5.87 V) | 4.5406 ms | 5870.0000 ms |
| V(vout) max | 6.52936 V | 6.52936 V |
| V(vout) average | 6.52120 V | 6.52080 V |
| V(vout) ripple (pk-pk) | 13.254 mV | 13.254 mV |
| I(L1) max | 1.91584 A | 1.91584 A |
| I(L1) ripple (pk-pk) | 0.7751 A | 0.7751 A |
| P(in) | 6.7079 W | 6.6936 W |
| P(out) | 6.5425 W | 6.5417 W |
| efficiency | 97.53 % | 97.730 % |

## How to regenerate
```
python make_charts.py
```
Requires `numpy` and `matplotlib`. The script reads the raw file directly; the
LTspice "fast access" binary layout used here is 48 bytes per point:

```
bytes  0.. 7   time          IEEE-754 double, little endian
bytes  8..11   V(bst)        float32
bytes 12..15   V(en)         float32
bytes 16..19   V(fb)         float32
bytes 20..23   V(ss)         float32
bytes 24..27   V(sw)         float32
bytes 28..31   V(vin)        float32
bytes 32..35   V(vout)       float32
bytes 36..39   I(L1)         float32
bytes 40..43   I(Rh)         float32
bytes 44..47   L1:flux       float32
```

### Layout guarantee
Figures are built with `constrained_layout=True`, and `make_charts.py` runs a
`check_layout()` pass after every figure. It measures the pixel bounding box of
every title, axis label, tick label, legend entry and annotation and fails loudly
if any two of them intersect, or if any text is clipped by the canvas edge.

A second, independent check runs on the finished SVG files themselves:

```
python verify_svg_layout.py
```

It parses each `.svg`, applies every SVG `transform` (including the 90 degree
rotation of the axis labels), measures the true string width with the real
DejaVu Sans font file that matplotlib ships, and reports any pair of text boxes
that intersect or any text that leaves the canvas. Current result:
**9 / 9 charts clean, 0 overlaps, 0 clipped labels.**
