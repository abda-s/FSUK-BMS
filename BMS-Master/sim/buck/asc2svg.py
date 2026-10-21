"""Render an LTspice .asc schematic to SVG using the real .asy symbol drawings.
usage: python asc2svg.py file.asc out.svg"""
import sys, os, math, html
from collections import Counter

asc_path, out_path = sys.argv[1], sys.argv[2]
SYMDIRS = [os.path.dirname(asc_path), os.path.join(os.environ["LOCALAPPDATA"], "LTspice", "lib", "sym")]
WIRE_C, SYM_C, TXT_C, CMT_C, DIR_C = "#1f4fd8", "#202020", "#202020", "#3a7a3a", "#202020"
FS = {0: 12, 1: 16, 2: 22, 3: 28}

def load_asy(name):
    for d in SYMDIRS:
        p = os.path.join(d, name.replace("\\\\", os.sep) + ".asy")
        if os.path.exists(p):
            sym = {"lines": [], "rects": [], "circles": [], "arcs": [], "texts": [], "pins": [], "win": {}}
            for raw in open(p, encoding="latin-1"):
                t = raw.split()
                if not t: continue
                k = t[0]
                if k == "LINE": sym["lines"].append(list(map(int, t[2:6])))
                elif k == "RECTANGLE": sym["rects"].append(list(map(int, t[2:6])))
                elif k == "CIRCLE": sym["circles"].append(list(map(int, t[2:6])))
                elif k == "ARC": sym["arcs"].append(list(map(int, t[2:10])))
                elif k == "TEXT": sym["texts"].append((int(t[1]), int(t[2]), t[3], int(t[4]), " ".join(t[5:])))
                elif k == "WINDOW": sym["win"][int(t[1])] = (int(t[2]), int(t[3]), t[4], int(t[5]))
                elif k == "PIN": sym["pins"].append([int(t[1]), int(t[2]), t[3], int(t[4]), ""])
                elif k == "PINATTR" and t[1] == "PinName": sym["pins"][-1][4] = t[2]
            return sym
    raise FileNotFoundError(name)

def tf(rot, sx, sy):
    m = {"R0": (1, 0, 0, 1), "R90": (0, -1, 1, 0), "R180": (-1, 0, 0, -1), "R270": (0, 1, -1, 0)}[rot]
    # R90: (sx - py, sy + px)  -> x' = -py, y' = px
    a, b, c, d = m
    return lambda x, y: (sx + a * x + b * y, sy + c * x + d * y)

wires, flags, syms, texts = [], [], [], []
cur = None
for raw in open(asc_path, encoding="latin-1"):
    t = raw.rstrip("\r\n").split(" ")
    k = t[0]
    if k == "WIRE": wires.append(tuple(map(int, t[1:5])))
    elif k == "FLAG": flags.append((int(t[1]), int(t[2]), t[3]))
    elif k == "SYMBOL":
        cur = {"name": t[1], "x": int(t[2]), "y": int(t[3]), "rot": t[4], "attr": {}, "win": {}}
        syms.append(cur)
    elif k == "WINDOW" and cur: cur["win"][int(t[1])] = (int(t[2]), int(t[3]), t[4], int(t[5]))
    elif k == "SYMATTR" and cur: cur["attr"][t[1]] = " ".join(t[2:])
    elif k == "TEXT":
        texts.append((int(t[1]), int(t[2]), t[3], int(t[4]), " ".join(t[5:])))

out, pts = [], []
def P(x, y): pts.append((x, y)); return f"{x},{y}"
def line(x1, y1, x2, y2, c, w=2):
    out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'); P(x1, y1); P(x2, y2)
def text(x, y, s, size, anchor="start", c=TXT_C, weight="normal", base="middle"):
    out.append(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" dominant-baseline="{base}" fill="{c}" font-weight="{weight}">{html.escape(s)}</text>')
    w = len(s) * size * 0.56
    x0 = x - (w if anchor == "end" else w / 2 if anchor == "middle" else 0)
    P(x0, y - size); P(x0 + w, y + size)

# ---- symbols ----
pin_pts = []
for s in syms:
    a = load_asy(s["name"]); T = tf(s["rot"], s["x"], s["y"])
    for x1, y1, x2, y2 in a["lines"]:
        X1, Y1 = T(x1, y1); X2, Y2 = T(x2, y2); line(X1, Y1, X2, Y2, SYM_C)
    for x1, y1, x2, y2 in a["rects"]:
        c = [T(x1, y1), T(x2, y2)]; xs = sorted(p[0] for p in c); ys = sorted(p[1] for p in c)
        out.append(f'<rect x="{xs[0]}" y="{ys[0]}" width="{xs[1]-xs[0]}" height="{ys[1]-ys[0]}" fill="#fffbe8" stroke="{SYM_C}" stroke-width="2"/>'); P(xs[0], ys[0]); P(xs[1], ys[1])
    for x1, y1, x2, y2 in a["circles"]:
        c = [T(x1, y1), T(x2, y2)]; cx = (c[0][0] + c[1][0]) / 2; cy = (c[0][1] + c[1][1]) / 2
        r = abs(c[0][0] - c[1][0]) / 2
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{SYM_C}" stroke-width="2"/>'); P(cx - r, cy - r); P(cx + r, cy + r)
    for x1, y1, x2, y2, x3, y3, x4, y4 in a["arcs"]:
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2; r = abs(x2 - x1) / 2
        a1 = math.atan2(-(y3 - cy), x3 - cx); a2 = math.atan2(-(y4 - cy), x4 - cx)  # math angles, CCW positive
        sweep = (a2 - a1) % (2 * math.pi)
        S = T(cx + r * math.cos(a1), cy - r * math.sin(a1)); E = T(cx + r * math.cos(a2), cy - r * math.sin(a2))
        out.append(f'<path d="M{S[0]:.1f},{S[1]:.1f} A{r},{r} 0 {1 if sweep > math.pi else 0} 0 {E[0]:.1f},{E[1]:.1f}" fill="none" stroke="{SYM_C}" stroke-width="2"/>')
        P(*S); P(*E)
    for tx, ty, j, sz, st in a["texts"]:
        X, Y = T(tx, ty); text(X, Y, st, FS[sz] if sz < 2 else 26, "middle", weight="bold" if sz >= 2 else "normal")
    for px, py, side, off, nm in a["pins"]:
        X, Y = T(px, py); pin_pts.append((X, Y))
        if s["name"] == "TPS62933F" and nm:
            if side == "LEFT": text(X + 12, Y, nm, 18)
            elif side == "RIGHT": text(X - 12, Y, nm, 18, "end")
            else: text(X, Y - 18, nm, 18, "middle")
    # attribute labels
    name, val = s["attr"].get("InstName", ""), s["attr"].get("Value", "")
    if s["name"] == "TPS62933F":
        text(s["x"], s["y"] - 184, name, 22, "middle", weight="bold"); continue
    xs = [p[0] for p in pts[-40:]]; ys = [p[1] for p in pts[-40:]]
    corners = [T(x, y) for x, y in [(0, 0), (32, 0), (0, 96), (32, 96)]] if s["name"] != "voltage" else [T(-32, 16), T(32, 96)]
    bx = [c[0] for c in corners]; by = [c[1] for c in corners]
    if s["rot"] in ("R90", "R270"):
        cx = (min(bx) + max(bx)) / 2
        text(cx, min(by) - 10, name, 20, "middle", weight="bold"); text(cx, max(by) + 14, val, 20, "middle")
    else:
        w0 = a["win"].get(0, (36, 40, "Left", 2)); w3 = a["win"].get(3, (36, 76, "Left", 2))
        w0 = s["win"].get(0, w0); w3 = s["win"].get(3, w3)
        X0, Y0 = T(w0[0], w0[1]); X3, Y3 = T(w3[0], w3[1])
        text(X0, Y0, name, 20, weight="bold"); text(X3, Y3, val, 20)
        spl = s["attr"].get("SpiceLine")
        if spl: text(X3, Y3 + 22, spl, 16, c="#555")

# ---- wires + junctions ----
for x1, y1, x2, y2 in wires: line(x1, y1, x2, y2, WIRE_C)
cnt = Counter()
for x1, y1, x2, y2 in wires: cnt[(x1, y1)] += 1; cnt[(x2, y2)] += 1
for p in pin_pts: cnt[p] += 1
for (x, y), n in cnt.items():
    if n >= 3: out.append(f'<rect x="{x-5}" y="{y-5}" width="10" height="10" fill="{WIRE_C}"/>')

# ---- flags ----
for x, y, n in flags:
    if n == "0":
        for dx, dy in [(-16, 0), (16, 0)]: pass
        out.append(f'<path d="M{x-20},{y} L{x+20},{y} L{x},{y+18} Z" fill="none" stroke="{SYM_C}" stroke-width="2"/>'); P(x - 20, y); P(x + 20, y + 18)
    else:
        text(x, y - 14, n, 20, "middle", c="#1f4fd8", weight="bold")
        out.append(f'<rect x="{x-4}" y="{y-4}" width="8" height="8" fill="none" stroke="{WIRE_C}" stroke-width="1.5"/>')

# ---- free text ----
for x, y, j, sz, s in texts:
    if s.startswith("!"): text(x, y, s[1:], FS[sz] - 2, c=DIR_C, base="middle")
    else: text(x, y, s.lstrip(";"), FS[sz], c=CMT_C)

X0 = min(p[0] for p in pts) - 30; Y0 = min(p[1] for p in pts) - 30
X1 = max(p[0] for p in pts) + 30; Y1 = max(p[1] for p in pts) + 30
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{X0:.0f} {Y0:.0f} {X1-X0:.0f} {Y1-Y0:.0f}" '
       f'width="{(X1-X0)*0.6:.0f}" height="{(Y1-Y0)*0.6:.0f}" font-family="Consolas, DejaVu Sans Mono, monospace">\n'
       f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" fill="#ffffff"/>\n' + "\n".join(out) + "\n</svg>\n")
open(out_path, "w", encoding="utf-8").write(svg)
print("ok", len(syms), "symbols", len(wires), "wires", f"bbox {X0:.0f},{Y0:.0f} {X1:.0f},{Y1:.0f}")
