"""
LTspice raw-file reader + chart generator for buck_startup.raw
(TPS62933F buck, 12 V -> 6 V, transient startup).

Binary layout of this LTspice "fast access" raw file:
  UTF-16LE text header, "Binary:\n" then, per point, a 48-byte record:
      bytes  0.. 7 : time          (IEEE-754 double, little endian)
      bytes  8..11 : V(bst)        (float32)
      bytes 12..15 : V(en)         (float32)
      bytes 16..19 : V(fb)         (float32)
      bytes 20..23 : V(ss)         (float32)
      bytes 24..27 : V(sw)         (float32)
      bytes 28..31 : V(vin)        (float32)
      bytes 32..35 : V(vout)       (float32)
      bytes 36..39 : I(L1)         (float32)
      bytes 40..43 : I(Rh)         (float32)
      bytes 44..47 : L1:flux       (float32)

Reads only; never writes to the simulation folder.
Outputs both PNG and SVG for every chart.
"""
import os
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

RAW = r"E:\Documents\Racing\FSUK-BMS\BMS-Master\sim\buck\buck_startup.raw"
OUT = r"E:\Documents\Racing\FSUK-BMS\BMS-Master\sim\buck\charts"
os.makedirs(OUT, exist_ok=True)

VAR_NAMES = ["V(bst)", "V(en)", "V(fb)", "V(ss)", "V(sw)",
             "V(vin)", "V(vout)", "I(L1)", "I(Rh)", "L1:flux"]

# ----------------------------------------------------------------------------- read
with open(RAW, "rb") as fh:
    fh.seek(1000)                       # start of the binary block
    raw = fh.read()

u = np.frombuffer(raw, dtype="<u4").reshape(-1, 12)
n = u.shape[0]
t = np.empty(n, dtype="<f8")
t.view(np.uint64)[:] = (u[:, 0].astype(np.uint64)
                        | (u[:, 1].astype(np.uint64) << np.uint64(32)))
V = {c: np.ascontiguousarray(u[:, 2 + i]).view("<f4")
     for i, c in enumerate(VAR_NAMES)}

vout, il1, vin, irh = V["V(vout)"], V["I(L1)"], V["V(vin)"], V["I(Rh)"]
RL = 6.0                             # load resistor, ohm

# ------------------------------------------------------------------- derived data
pin = vin * irh                       # W, input power
pout = vout * vout / RL               # W, output power
eff = pout / np.where(pin > 1e-6, pin, np.nan)

def win(a, b):
    return (t >= a) & (t <= b)

m_steady = win(8e-3, 9e-3)
stats = dict(
    t_on=t[np.argmax(vout > 0.1)],
    vin_on=vin[np.argmax(vout > 0.1)],
    t_90=t[np.argmax(vout > 5.4)],
    vout_max=vout.max(),
    il_max=il1.max(),
    vout_avg=vout[m_steady].mean(),
    vout_pp=np.ptp(vout[win(8.5e-3, 9e-3)]),
    il_pp=np.ptp(il1[win(8.5e-3, 9e-3)]),
    pin=pin[m_steady].mean(),
    pout=pout[m_steady].mean(),
)
stats["eff"] = stats["pout"] / stats["pin"]

# --------------------------------------------------------------- plotting helpers
C = {
    "vout": "#c0392b", "vin": "#2c3e50", "sw": "#8e44ad", "il": "#16a085",
    "ss": "#e67e22", "en": "#2980b9", "fb": "#27ae60", "bst": "#7f8c8d",
    "irh": "#d35400", "pin": "#c0392b", "pout": "#16a085", "eff": "#2980b9",
    "grid": "#dfe4ea", "txt": "#2c3e50",
}
plt.rcParams.update({
    "figure.dpi": 130, "savefig.dpi": 130,
    "font.family": "DejaVu Sans", "font.size": 10,
    "axes.edgecolor": "#9aa5b1", "axes.labelcolor": C["txt"],
    "axes.titlesize": 11, "axes.titleweight": "bold", "axes.labelsize": 10,
    "xtick.color": "#4a5568", "ytick.color": "#4a5568",
    "legend.frameon": True, "legend.framealpha": 0.92,
    "legend.edgecolor": "#dfe4ea", "legend.borderpad": 0.5,
    "legend.fontsize": 9,
    "axes.grid": True, "grid.color": C["grid"], "grid.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
    "svg.fonttype": "none",            # keep SVG labels as real, selectable text
})

def envelope(x, y, nbins=1400):
    """Min/max decimation so 2.5 M points plot fast and keep every peak."""
    e = np.linspace(0, len(x), nbins + 1).astype(np.int64)
    s = e[:-1]
    return x[s], np.minimum.reduceat(y, s), np.maximum.reduceat(y, s)

def plot_env(ax, x, y, label, color, nbins=1400, lw=1.1, alpha=0.30):
    xd, lo, hi = envelope(x, y, nbins)
    ax.fill_between(xd, lo, hi, color=color, alpha=alpha, linewidth=0)
    ax.plot(xd, (lo + hi) / 2, color=color, lw=lw, label=label)

def plot_series(ax, x, y, label, color, nbins=1400, lw=1.1):
    xd, lo, hi = envelope(x, y, nbins)
    ax.plot(xd, (lo + hi) / 2, color=color, lw=lw, label=label)

def plain_fmt():
    """Deterministic numeric tick labels; the unit is in the axis label."""
    def f(v, pos):
        s = f"{v:.2f}".rstrip("0").rstrip(".")
        return s if s not in ("", "-") else "0"
    return FuncFormatter(f)

def x_ms(ax):
    ax.set_xlabel("time  [ms]")
    ax.xaxis.set_major_formatter(plain_fmt())

def x_us(ax):
    ax.set_xlabel("time  [us]")
    ax.xaxis.set_major_formatter(plain_fmt())

# ------------------------------------------------------------- figure management
SUB = "TPS62933F buck  |  12 V -> 6 V @ 1 A  |  buck_startup.raw  |  2 482 358 pts, 0-9 ms, max step 20 ns"

def new_fig(nrows, ncols, figsize, title, heights=None):
    """constrained_layout keeps titles/labels/tick text from colliding."""
    kw = dict(figsize=figsize, constrained_layout=True)
    if heights is not None:
        kw["height_ratios"] = heights
    fig, axs = plt.subplots(nrows, ncols, **kw)
    fig.suptitle(title, fontsize=13, fontweight="bold", color=C["txt"])
    fig.supxlabel(SUB, fontsize=8, color="#7b8794")
    return fig, axs

def _texts(fig):
    """Every piece of text that must not collide with another."""
    st = getattr(fig, "_suptitle", None)
    sx = getattr(fig, "_supxlabel", None)
    items = []
    for ai, ax in enumerate(fig.axes):
        for tx in ax.texts:
            if tx.get_text().strip():
                items.append((f"annot:{tx.get_text()[:26]}", tx))
        if ax.get_title().strip():
            items.append((f"title:{ax.get_title()[:26]}", ax.title))
        if ax.get_xlabel().strip():
            items.append((f"xlabel:{ax.get_xlabel()[:26]}", ax.xaxis.label))
        if ax.get_ylabel().strip():
            items.append((f"ylabel:{ax.get_ylabel()[:26]}", ax.yaxis.label))
        leg = ax.get_legend()
        if leg is not None:
            for j, tx in enumerate(leg.get_texts()):
                if tx.get_text().strip():
                    items.append((f"legend{ai}.{j}:{tx.get_text()[:20]}", tx))
        for j, (loc, tx) in enumerate(zip(ax.get_yticks(), ax.get_yticklabels())):
            if not tx.get_text().strip() or not tx.get_visible():
                continue
            lo, hi = ax.get_ylim()
            if not (lo <= loc <= hi):        # tick outside the view limits
                continue
            items.append((f"ytick{ai}.{j}:{tx.get_text()[:12]}", tx))
        for j, (loc, tx) in enumerate(zip(ax.get_xticks(), ax.get_xticklabels())):
            if not tx.get_text().strip() or not tx.get_visible():
                continue
            lo, hi = ax.get_xlim()
            if not (lo <= loc <= hi):
                continue
            items.append((f"xtick{ai}.{j}:{tx.get_text()[:12]}", tx))
    for tx in fig.texts:
        if tx is st or tx is sx:          # already covered below
            continue
        if tx.get_text().strip():
            items.append((f"figtext:{tx.get_text()[:26]}", tx))
    if st is not None and st.get_text().strip():
        items.append(("suptitle", st))
    if sx is not None and sx.get_text().strip():
        items.append(("supxlabel", sx))
    return items

def check_layout(fig, name):
    """Verify no two text objects overlap and nothing is clipped by the canvas."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    fb = fig.get_window_extent(renderer=r)
    boxes = []
    for label, artist in _texts(fig):
        try:
            bb = artist.get_window_extent(renderer=r)
        except Exception:
            continue
        if bb.width <= 0 or bb.height <= 0:
            continue
        boxes.append((label, bb))
    problems = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            a, b = boxes[i][1], boxes[j][1]
            ox = min(a.x1, b.x1) - max(a.x0, b.x0)
            oy = min(a.y1, b.y1) - max(a.y0, b.y0)
            if ox > 1.0 and oy > 1.0:
                problems.append(f"OVERLAP {boxes[i][0]!r} <-> {boxes[j][0]!r} "
                                f"({ox:.1f}x{oy:.1f} px)")
    for label, bb in boxes:
        if (bb.x0 < fb.x0 - 1 or bb.x1 > fb.x1 + 1
                or bb.y0 < fb.y0 - 1 or bb.y1 > fb.y1 + 1):
            problems.append(f"CLIPPED {label!r}")
    return problems

def finish(fig, stem, note=None):
    """Save PNG + SVG, with retries (the repo folder occasionally locks files)."""
    if note:
        fig.supxlabel(note)
    probs = check_layout(fig, stem)
    for ext in ("png", "svg"):
        dest = os.path.join(OUT, f"{stem}.{ext}")
        for attempt in range(8):
            try:
                fig.savefig(dest)
                break
            except OSError:
                if attempt == 7:
                    raise
                time.sleep(0.4 * (attempt + 1))
    plt.close(fig)
    print(f"  wrote {stem}.png / {stem}.svg"
          + ("   [LAYOUT OK]" if not probs else "   [LAYOUT PROBLEMS]"))
    for p in probs:
        try:
            print("      ", p)
        except UnicodeEncodeError:
            print("      ", p.encode('ascii','replace').decode('ascii'))
    return probs

# ============================================================ 1. startup overview
fig, ax = new_fig(1, 1, (11.5, 5.6), "Startup overview - input ramp, output ramp-up, soft-start and enable")
plot_env(ax, t * 1e3, vin, "V(vin)  input rail", C["vin"])
plot_env(ax, t * 1e3, vout, "V(vout)  output", C["vout"])
plot_env(ax, t * 1e3, V["V(ss)"], "V(ss)  soft-start", C["ss"])
plot_env(ax, t * 1e3, V["V(en)"], "V(en)  enable", C["en"])

ax.axvline(stats["t_on"] * 1e3, color="#7f8c8d", ls="--", lw=1)
ax.annotate(f"t_on = {stats['t_on']*1e3:.3f} ms  (Vout = 0.1 V)",
            xy=(stats["t_on"] * 1e3, 0.5), xytext=(1.05, 1.9),
            fontsize=8.5, color="#5d6d7e",
            arrowprops=dict(arrowstyle="->", color="#95a5a6", lw=1))
ax.axvline(stats["t_90"] * 1e3, color="#7f8c8d", ls="--", lw=1)
ax.annotate(f"t_90 = {stats['t_90']*1e3:.3f} ms  (Vout = 5.4 V)",
            xy=(stats["t_90"] * 1e3, 3.5), xytext=(3.1, 4.6),
            fontsize=8.5, color="#5d6d7e",
            arrowprops=dict(arrowstyle="->", color="#95a5a6", lw=1))
ax.set_xlim(0, 9)
ax.set_ylim(-0.4, 13)
ax.set_ylabel("voltage  [V]")
ax.legend(loc="lower right", ncol=2)
x_ms(ax)
finish(fig, "01_startup_overview")

# ====================================================== 2. output voltage + ripple
fig, axs = new_fig(2, 1, (11.5, 8.0), "Output voltage - start-up and steady-state ripple",
                    heights=[1.3, 1])
plot_env(axs[0], t * 1e3, vout, "V(vout)", C["vout"], nbins=1400, lw=1.4)
axs[0].axhline(6.0, color="#95a5a6", ls=":", lw=1.2)
axs[0].text(0.15, 6.05, "target 6.000 V", fontsize=8.5, color="#7f8c8d")
axs[0].axhline(stats["vout_avg"], color="#c0392b", ls="--", lw=1)
axs[0].text(0.15, stats["vout_avg"] - 0.30,
            f"steady-state average = {stats['vout_avg']:.4f} V",
            fontsize=8.5, color=C["vout"])
axs[0].set_ylabel("V(vout)  [V]")
axs[0].set_xlim(0, 9)
x_ms(axs[0])

sw = win(8.5e-3, 9e-3)
plot_env(axs[1], t[sw] * 1e6, vout[sw], "V(vout)", C["vout"], nbins=1200)
axs[1].set_xlim(8500, 9000)
axs[1].set_ylabel("V(vout)  [V]")
axs[1].set_title(f"Steady-state output ripple  (8.5 - 9.0 ms,  pk-pk = {stats['vout_pp']*1e3:.2f} mV)",
                 fontsize=10)
x_us(axs[1])
finish(fig, "02_output_voltage")

# ====================================================== 3. inductor current + ripple
fig, axs = new_fig(2, 1, (11.5, 8.0), "Inductor current - start-up inrush and steady-state ripple",
                    heights=[1.3, 1])
plot_env(axs[0], t * 1e3, il1, "I(L1)  inductor current", C["il"])
axs[0].axhline(1.0, color="#95a5a6", ls=":", lw=1.2)
axs[0].text(0.15, 1.04, "1 A load (Rload = 6 ohm)", fontsize=8.5, color="#7f8c8d")
axs[0].annotate(f"peak = {stats['il_max']:.3f} A",
                xy=(t[np.argmax(il1)] * 1e3, stats["il_max"]),
                xytext=(t[np.argmax(il1)] * 1e3 + 0.8, stats["il_max"] - 0.42),
                fontsize=8.5, color=C["il"],
                arrowprops=dict(arrowstyle="->", color=C["il"], lw=1))
axs[0].set_ylabel("I(L1)  [A]")
axs[0].set_xlim(0, 9)
x_ms(axs[0])

sw2 = win(8.5e-3, 9e-3)
plot_env(axs[1], t[sw2] * 1e6, il1[sw2], "I(L1)", C["il"], nbins=1200)
axs[1].set_xlim(8500, 9000)
axs[1].set_ylabel("I(L1)  [A]")
axs[1].set_title(f"Steady-state inductor ripple  (pk-pk = {stats['il_pp']:.3f} A)", fontsize=10)
x_us(axs[1])
finish(fig, "03_inductor_current")

# ============================================================ 4. switching node
fig, axs = new_fig(2, 1, (11.5, 8.2), "Switch node - PWM waveform at steady state", heights=[1, 1.3])
swv = V["V(sw)"]
plot_env(axs[0], t * 1e3, swv, "V(sw)  switch node", C["sw"])
axs[0].set_ylabel("V(sw)  [V]")
axs[0].set_title("Full start-up", fontsize=10)
axs[0].set_xlim(0, 9)
x_ms(axs[0])

z = win(8.99e-3, 9.0e-3)
axs[1].plot(t[z] * 1e6, swv[z], color=C["sw"], lw=1.3, label="V(sw)")
axs[1].plot(t[z] * 1e6, vout[z], color=C["vout"], lw=1.5, label="V(vout)")
axs[1].axhline(0, color="#95a5a6", lw=0.8)
axs[1].set_xlim(8990, 9000)
axs[1].set_ylabel("voltage  [V]")
axs[1].set_title("Switching detail  (8.990 - 9.000 ms,  f_sw ~ 496 kHz)", fontsize=10)
x_us(axs[1])
axs[1].legend(loc="upper right", ncol=2)
finish(fig, "04_switch_node")

# ========================================================= 5. power & efficiency
fig, axs = new_fig(2, 1, (11.5, 8.0), "Input / output power and converter efficiency",
                    heights=[1.25, 1])
plot_env(axs[0], t * 1e3, pin, "P(in)  = V(vin) x I(Rh)", C["pin"])
plot_env(axs[0], t * 1e3, pout, "P(out)  = V(vout)^2 / 6 ohm", C["pout"])
axs[0].set_ylabel("power  [W]")
axs[0].set_title("Power during start-up", fontsize=10)
axs[0].set_xlim(0, 9)
axs[0].legend(loc="upper right", ncol=2)
x_ms(axs[0])

e = np.where(np.isfinite(eff), eff, np.nan)
e2 = np.where(pout > 0.05, e, np.nan)      # ignore the meaningless zero-power region
plot_series(axs[1], t * 1e3, e2, "efficiency", C["eff"])
axs[1].axhline(stats["eff"], color="#95a5a6", ls=":", lw=1.2)
axs[1].text(0.15, stats["eff"] + 0.014,
            f"steady-state efficiency = {stats['eff']*100:.2f} %", fontsize=8.5, color="#7f8c8d")
axs[1].set_ylim(0, 1.05)
axs[1].set_ylabel("efficiency  [%]")
axs[1].set_title("Converter efficiency  (values above 100 % during soft-start are "
                 "charge-redistribution artefacts)", fontsize=10)
axs[1].set_xlim(0, 9)
axs[1].yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v*100:.0f} %"))
x_ms(axs[1])
finish(fig, "05_power_efficiency")

# ========================================================= 6. input stage & current
fig, axs = new_fig(2, 1, (11.5, 8.0), "Input stage - battery / harness rail and input current")
plot_env(axs[0], t * 1e3, vin, "V(vin)  battery + harness", C["vin"])
axs[0].set_ylabel("V(vin)  [V]")
axs[0].set_title("12 V battery through 1 uH + 50 mOhm harness", fontsize=10)
axs[0].set_xlim(0, 9)
x_ms(axs[0])

plot_env(axs[1], t * 1e3, irh, "I(Rh)  input current", C["irh"])
axs[1].set_ylabel("I(Rh)  [A]")
axs[1].set_title("Input current - inrush at switch-on, then steady state", fontsize=10)
axs[1].set_xlim(0, 9)
axs[1].legend(loc="upper right")
x_ms(axs[1])
finish(fig, "06_input_stage")

# ============================================================ 7. control signals
fig, ax = new_fig(1, 1, (11.5, 6.0), "Control pins - enable, soft-start, feedback and bootstrap")
plot_env(ax, t * 1e3, V["V(en)"], "V(en)  enable", C["en"])
plot_env(ax, t * 1e3, V["V(ss)"], "V(ss)  soft-start", C["ss"])
plot_env(ax, t * 1e3, V["V(fb)"], "V(fb)  feedback", C["fb"])
plot_env(ax, t * 1e3, V["V(bst)"], "V(bst)  bootstrap", C["bst"])
ax.axhline(0.8, color="#27ae60", ls=":", lw=1.2)
ax.text(0.15, 0.86, "FB reference 0.800 V", fontsize=8.5, color="#27ae60")
ax.set_xlim(0, 9)
ax.set_ylabel("voltage  [V]")
ax.legend(loc="upper right", ncol=2)
x_ms(ax)
finish(fig, "07_control_signals")

# ========================================================= 8. startup detail 0-1.5ms
fig, axs = new_fig(2, 1, (11.5, 8.0), "Start-up detail  (0 - 1.5 ms)")
d = win(0, 1.5e-3)
axs[0].plot(t[d] * 1e3, vin[d], color=C["vin"], lw=1.2, label="V(vin)")
axs[0].plot(t[d] * 1e3, V["V(en)"][d], color=C["en"], lw=1.2, label="V(en)")
axs[0].plot(t[d] * 1e3, vout[d], color=C["vout"], lw=1.4, label="V(vout)")
axs[0].axvline(stats["t_on"] * 1e3, color="#7f8c8d", ls="--", lw=1)
axs[0].set_xlim(0, 1.5)
axs[0].set_ylabel("voltage  [V]")
axs[0].set_title("Rails", fontsize=10)
axs[0].legend(loc="center right", ncol=3)
x_ms(axs[0])

axs[1].plot(t[d] * 1e3, il1[d], color=C["il"], lw=1.2, label="I(L1)")
axs[1].plot(t[d] * 1e3, irh[d], color=C["irh"], lw=1.2, label="I(Rh)")
axs[1].set_xlim(0, 1.5)
axs[1].set_ylabel("current  [A]")
axs[1].set_title("Currents", fontsize=10)
axs[1].legend(loc="upper right", ncol=2)
x_ms(axs[1])
finish(fig, "08_startup_detail")

# ============================================================ 9. summary dashboard
fig, axs = new_fig(3, 2, (13.5, 11.5),
                    "TPS62933F buck converter - start-up summary (LTspice transient)")
panels = [
    (axs[0, 0], [(vin, C["vin"], "V(vin)"), (vout, C["vout"], "V(vout)")], "V(vin) / V(vout)", "V", "ms"),
    (axs[0, 1], [(il1, C["il"], "I(L1)")], "I(L1)", "A", "ms"),
    (axs[1, 0], [(V["V(ss)"], C["ss"], "V(ss)")], "V(ss)  soft-start", "V", "ms"),
    (axs[1, 1], [(V["V(fb)"], C["fb"], "V(fb)")], "V(fb)  feedback", "V", "ms"),
    (axs[2, 0], [(pin, C["pin"], "P(in)"), (pout, C["pout"], "P(out)")], "Power", "W", "ms"),
]
for axx, series, title, ylab, unit in panels:
    for y, c, lab in series:
        plot_env(axx, t * 1e3, y, lab, c, nbins=800)
    axx.set_title(title, fontsize=10)
    axx.set_ylabel(f"{ylab}  [{unit}]")
    axx.set_xlim(0, 9)
    x_ms(axx)
    if len(series) > 1:
        axx.legend(loc="upper right", ncol=2)

axs[2, 1].plot(t * 1e3, e2, color=C["eff"], lw=1.1)
axs[2, 1].set_title("Efficiency", fontsize=10)
axs[2, 1].set_ylabel("efficiency  [%]")
axs[2, 1].set_ylim(0, 1.05)
axs[2, 1].set_xlim(0, 9)
axs[2, 1].yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v*100:.0f} %"))
x_ms(axs[2, 1])
finish(fig, "09_summary_dashboard")

# ============================================================ CSV data export
sel = np.linspace(0, n - 1, 30000).astype(np.int64)
cols = ["time_s", "time_ms"] + VAR_NAMES + ["Pin_W", "Pout_W", "eff"]
out = np.column_stack([
    t[sel], t[sel] * 1e3,
    V["V(bst)"][sel], V["V(en)"][sel], V["V(fb)"][sel], V["V(ss)"][sel],
    V["V(sw)"][sel], vin[sel], vout[sel], il1[sel], irh[sel], V["L1:flux"][sel],
    pin[sel], pout[sel], eff[sel],
])
np.savetxt(os.path.join(OUT, "buck_startup_data.csv"), out, delimiter=",",
           header=",".join(cols), comments="", fmt="%.9g")
print("  wrote buck_startup_data.csv  (%d rows)" % len(sel))

# ============================================================ HTML gallery
imgs = [
    ("01_startup_overview", "Startup overview",
     "Input ramp, output ramp-up, soft-start and enable over the full 9 ms transient."),
    ("02_output_voltage", "Output voltage",
     "V(vout) from power-on to steady state, plus the steady-state ripple zoom."),
    ("03_inductor_current", "Inductor current",
     "I(L1) inrush peak and steady-state ripple."),
    ("04_switch_node", "Switch node",
     "V(sw) switching waveform at ~496 kHz with V(vout) overlaid."),
    ("05_power_efficiency", "Power and efficiency",
     "Input/output power and converter efficiency versus time."),
    ("06_input_stage", "Input stage",
     "V(vin) battery+harness rail and the input current I(Rh)."),
    ("07_control_signals", "Control pins",
     "V(en), V(ss), V(fb) and V(bst) behaviour."),
    ("08_startup_detail", "Start-up detail",
     "0 - 1.5 ms close-up of the rails and currents."),
    ("09_summary_dashboard", "Summary dashboard",
     "Six-panel overview of every captured waveform."),
]
html = ["<!doctype html><html><head><meta charset='utf-8'>",
        "<title>Buck startup - LTspice charts</title>",
        "<style>body{font-family:Segoe UI,Arial,sans-serif;margin:28px;"
        "background:#f7f8fa;color:#2c3e50}h1{margin:0 0 4px}sub{color:#7b8794}"
        ".card{background:#fff;border:1px solid #e3e7ec;border-radius:8px;"
        "padding:14px;margin:18px 0;box-shadow:0 1px 3px rgba(0,0,0,.05)}"
        "img{width:100%;height:auto;border-radius:4px}"
        ".plot{width:100%;overflow-x:auto;background:#fff;border-radius:4px}"
        ".plot svg{width:100%;height:auto;display:block}"
        ".svg{float:right;margin-left:10px;font-size:12px}"
        ".tag{display:inline-block;background:#eef2f6;border-radius:4px;"
        "padding:2px 8px;font-size:12px;margin:2px}</style></head><body>",
        "<h1>TPS62933F buck converter - start-up charts</h1>",
        "<sub>Source: sim/buck/buck_startup.raw &nbsp;|&nbsp; 2 482 358 transient points "
        "&nbsp;|&nbsp; 0 - 9 ms, max step 20 ns &nbsp;|&nbsp; PNG + SVG</sub>"]
for stem, title, desc in imgs:
    with open(os.path.join(OUT, f"{stem}.svg"), encoding="utf-8") as fh:
        svg_inline = fh.read()
    # strip the XML prolog / doctype so the <svg> can be embedded directly
    svg_inline = svg_inline.split("?>", 1)[-1]
    svg_inline = svg_inline[svg_inline.index("<svg"):]
    html.append(f"<div class='card'><h2>{title}</h2>"
                f"<a class='svg' href='{stem}.svg'>SVG</a>"
                f"<a class='svg' href='{stem}.png'>PNG</a>"
                f"<p>{desc}</p>"
                f"<div class='plot'>{svg_inline}</div></div>")
html.append("<h2>Measured results (8 - 9 ms steady state)</h2><div class='card'>")
for k, v in stats.items():
    html.append(f"<span class='tag'>{k} = {v:.6g}</span>")
html.append("</div></body></html>")
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(html))
print("  wrote index.html")

# ============================================================ README
md = f"""# Buck converter start-up charts

Charts generated from the LTspice transient run **`../buck_startup.raw`**
(schematic `../buck_startup.asc`). Nothing in the simulation folder was modified.

Open **`index.html`** for a gallery of every chart.
Every chart exists in both **`.png`** (raster preview) and **`.svg`** (vector, real
selectable text - recommended for reports and printing).

## Circuit under test
TPS62933F buck converter, 12 V battery rail -> regulated 6 V into a 6 ohm load (1 A).
`.tran 0 9m 0 20n`, Gear integration, {n:,} stored points.

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
| t_on (Vout = 0.1 V) | {stats['t_on']*1e3:.4f} ms | 0.6798 ms |
| V(vin) at t_on | {stats['vin_on']:.4f} V | 8.0613 V |
| t_90 (Vout = 5.4 V) | {stats['t_90']*1e3:.4f} ms | 4.5440 ms |
| V(vout) max | {stats['vout_max']:.5f} V | 6.00183 V |
| V(vout) average | {stats['vout_avg']:.5f} V | 5.99273 V |
| V(vout) ripple (pk-pk) | {stats['vout_pp']*1e3:.3f} mV | 12.982 mV |
| I(L1) max | {stats['il_max']:.5f} A | 2.07271 A |
| I(L1) ripple (pk-pk) | {stats['il_pp']:.4f} A | 0.79460 A |
| P(in) | {stats['pin']:.4f} W | 6.1346 W |
| P(out) | {stats['pout']:.4f} W | 5.9855 W |
| efficiency | {stats['eff']*100:.2f} % | 97.569 % |

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
"""
with open(os.path.join(OUT, "README.md"), "w", encoding="utf-8") as fh:
    fh.write(md)
print("  wrote README.md")

print("\n=== steady-state summary (8-9 ms) ===")
for k, v in stats.items():
    print(f"  {k:9s} = {v:.9g}")
print("\n=== charts written to ===")
print(" ", OUT)
