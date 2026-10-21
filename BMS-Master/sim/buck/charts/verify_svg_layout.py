"""
Independent layout verification of the generated SVG charts.

Parses every .svg, extracts each <text> element, applies its SVG transform
(translate / rotate, including rotation about a centre point), measures the
true rendered width with the actual DejaVu Sans file that matplotlib ships,
builds the rotated bounding box, then reports:
  * any pair of text boxes that intersect  -> overlapping labels/titles
  * any text box that leaves the canvas    -> clipped text
"""
import glob
import math
import os
import re
import xml.etree.ElementTree as ET

from PIL import ImageFont
import matplotlib

FONT_DIR = os.path.join(os.path.dirname(matplotlib.__file__),
                        "mpl-data", "fonts", "ttf")
FONT_PATH = os.path.join(FONT_DIR, "DejaVuSans.ttf")
FONT_BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
SVG_NS = "{http://www.w3.org/2000/svg}"

OUT = r"E:\Documents\Racing\FSUK-BMS\BMS-Master\sim\buck\charts"

_font_cache = {}


def font_for(size, bold):
    key = (round(size, 1), bold)
    if key not in _font_cache:
        path = FONT_BOLD if bold else FONT_PATH
        _font_cache[key] = ImageFont.truetype(path, max(1, int(round(size))))
    return _font_cache[key]


def parse_style(style):
    out = {}
    for part in (style or "").split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            out[k.strip()] = v.strip()
    return out


# ---- 2-D affine matrices as (a, b, c, d, e, f):  x' = a*x + c*y + e ; y' = b*x + d*y + f
def m_ident():
    return (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)


def m_mul(m, n):                      # apply n first, then m
    a1, b1, c1, d1, e1, f1 = m
    a2, b2, c2, d2, e2, f2 = n
    return (a1 * a2 + c1 * b2,
            b1 * a2 + d1 * b2,
            a1 * c2 + c1 * d2,
            b1 * c2 + d1 * d2,
            a1 * e2 + c1 * f2 + e1,
            b1 * e2 + d1 * f2 + f1)


def m_translate(tx, ty):
    return (1.0, 0.0, 0.0, 1.0, tx, ty)


def m_rotate(deg):
    r = math.radians(deg)
    return (math.cos(r), math.sin(r), -math.sin(r), math.cos(r), 0.0, 0.0)


def parse_transform(t):
    if not t:
        return m_ident()
    m = m_ident()
    for name, args in re.findall(r"(\w+)\(([^)]*)\)", t):
        vals = [float(v) for v in re.split(r"[,\s]+", args.strip()) if v]
        if name == "translate":
            m = m_mul(m, m_translate(vals[0], vals[1] if len(vals) > 1 else 0.0))
        elif name == "rotate":
            if len(vals) >= 3:
                cx, cy = vals[1], vals[2]
                m = m_mul(m_mul(m_mul(m, m_translate(cx, cy)),
                                m_rotate(vals[0])),
                          m_translate(-cx, -cy))
            else:
                m = m_mul(m, m_rotate(vals[0]))
    return m


def apply(m, x, y):
    a, b, c, d, e, f = m
    return (a * x + c * y + e, b * x + d * y + f)


def collect(svg_path):
    root = ET.parse(svg_path).getroot()
    vb = root.get("viewBox")
    canvas = tuple(float(v) for v in vb.split())
    boxes = []
    for el in root.iter(f"{SVG_NS}text"):
        style = parse_style(el.get("style"))
        size = float(re.sub(r"[^0-9.]", "", style.get("font-size", "10")) or 10)
        anchor = style.get("text-anchor", "start")
        bold = ("Bold" in style.get("font-family", "")
                or style.get("font-weight", "") in ("bold", "700"))
        font = font_for(size, bold)
        asc, desc = font.getmetrics()

        # a <text> may hold one <tspan> per line
        spans = list(el.iter(f"{SVG_NS}tspan"))
        if spans:
            items = []
            for sp in spans:
                txt = "".join(sp.itertext())
                sx = float(sp.get("x", el.get("x", 0)))
                sy = float(sp.get("y", el.get("y", 0)))
                items.append((txt, sx, sy))
        else:
            items = [("".join(el.itertext()),
                      float(el.get("x", 0)), float(el.get("y", 0)))]

        # the element-level transform applies to the whole text block
        m_el = parse_transform(el.get("transform"))
        for txt, sx, sy in items:
            if not txt.strip():
                continue
            m = m_el
            tsp_tr = sp.get("transform") if spans else None
            if tsp_tr:
                m = m_mul(m_el, parse_transform(tsp_tr))
            w = font.getlength(txt)
            ax, ay = apply(m, sx, sy)
            # local text direction / perpendicular = LINEAR part of the matrix only
            ma, mb, mc, md, _, _ = m
            ux, uy = ma, mb
            vx, vy = mc, md
            ul = math.hypot(ux, uy) or 1.0
            ux, uy = ux / ul, uy / ul
            s0 = -w / 2.0 if anchor == "middle" else (-w if anchor == "end" else 0.0)
            corners = []
            for uu, vv in ((s0, -asc), (s0 + w, -asc), (s0, desc), (s0 + w, desc)):
                corners.append((ax + ux * uu + vx * vv, ay + uy * uu + vy * vv))
            xs = [c[0] for c in corners]
            ys = [c[1] for c in corners]
            boxes.append((txt, min(xs), min(ys), max(xs), max(ys)))
    return canvas, boxes


def overlaps(a, b):
    ox = min(a[3], b[3]) - max(a[1], b[1])
    oy = min(a[4], b[4]) - max(a[2], b[2])
    return (ox, oy) if (ox > 0.5 and oy > 0.5) else None


total = 0
for p in sorted(glob.glob(os.path.join(OUT, "*.svg"))):
    canvas, boxes = collect(p)
    cx, cy, cw, ch = canvas
    problems = []
    for i, a in enumerate(boxes):
        if (a[1] < cx - 0.5 or a[3] > cx + cw + 0.5
                or a[2] < cy - 0.5 or a[4] > cy + ch + 0.5):
            problems.append(f"CLIPPED {a[0][:36]!r} box=({a[1]:.1f},{a[2]:.1f})-({a[3]:.1f},{a[4]:.1f})")
        for b in boxes[i + 1:]:
            r = overlaps(a, b)
            if r:
                problems.append(f"OVERLAP {a[0][:26]!r} <-> {b[0][:26]!r} ({r[0]:.1f}x{r[1]:.1f} pt)")
    total += len(problems)
    print(f"{os.path.basename(p):30s} text-els={len(boxes):4d}  canvas={cw:.0f}x{ch:.0f}pt  "
          + ("OK - no overlaps, nothing clipped" if not problems else f"{len(problems)} PROBLEM(S)"))
    for q in problems[:15]:
        print("      ", q)

print()
print("TOTAL PROBLEMS:", total)
