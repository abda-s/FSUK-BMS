"""Draw an LQFP64 pinout in CubeMX style from the CubeMX MCU database + the project .ioc."""
import sys
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

DB = r"C:\Program Files\STMicroelectronics\STM32Cube\STM32CubeMX\db\mcu\STM32G474R(B-C-E)Tx.xml"
# usage: python make_pinout.py ../BMS-Master/BMS-Master.ioc pinout.svg
IOC, OUT = sys.argv[1], sys.argv[2]

root = ET.parse(DB).getroot()
ns = {"m": root.tag.split("}")[0].strip("{")}
pins = {}
for p in root.findall("m:Pin", ns):
    pins[int(p.get("Position"))] = (p.get("Name"), p.get("Type"))

kv = dict(l.split("=", 1) for l in open(IOC, encoding="utf-8").read().splitlines()[1:] if "=" in l)

def info(name):
    sig = kv.get(f"{name}.Signal")
    if not sig:
        return None, None
    label = kv.get(f"{name}.GPIO_Label")
    if not label:
        label = {"GPXTI0": "GPIO_EXTI0"}.get(sig, sig)
    return sig, label

N = 16                      # pins per side
P = 32                      # pin pitch
BW, BH = 26, 50             # pin box: width across pitch, length
BODY = N * P + 40           # chip body size
OX, OY = 330, 330           # body top-left
W = H = BODY + 2 * OX

C_USED, C_PWR, C_FREE, C_LINE = "#2fd35d", "#fff4c2", "#c8cdd2", "#555b61"
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Arial, Helvetica, sans-serif">',
       f'<rect width="100%" height="100%" fill="#ffffff"/>',
       f'<rect x="{OX}" y="{OY}" width="{BODY}" height="{BODY}" rx="6" fill="#5b6066" stroke="#3b4045" stroke-width="2"/>',
       f'<circle cx="{OX+22}" cy="{OY+22}" r="7" fill="#7b8086" stroke="#a7acb1"/>',
       f'<text x="{OX+BODY/2}" y="{OY+BODY/2-6}" font-size="30" fill="#ffffff" text-anchor="middle">STM32G474RETx</text>',
       f'<text x="{OX+BODY/2}" y="{OY+BODY/2+34}" font-size="24" font-style="italic" fill="#ffffff" text-anchor="middle">LQFP64</text>']

def pin_box(pos):
    i = (pos - 1) % N
    side = (pos - 1) // N            # 0 left (top->bottom), 1 bottom (L->R), 2 right (B->T), 3 top (R->L)
    off = 20 + i * P + P / 2
    if side == 0:  cx, cy = OX - BH / 2, OY + off
    elif side == 1: cx, cy = OX + off, OY + BODY + BH / 2
    elif side == 2: cx, cy = OX + BODY + BH / 2, OY + BODY - off
    else:           cx, cy = OX + BODY - off, OY - BH / 2
    return side, cx, cy

for pos in range(1, 4 * N + 1):
    name, typ = pins[pos]
    short = name.split("-")[0] if typ == "I/O" else name.split("-")[0]
    sig, label = info(name)
    fill = C_USED if sig else (C_PWR if typ in ("Power", "Reset", "Boot") and name.startswith(("V",)) else C_FREE)
    if name.startswith("VREF"):
        fill = "#bfe9c8"
    side, cx, cy = pin_box(pos)
    vertical = side in (1, 3)
    w, h = (BW, BH) if vertical else (BH, BW)
    out.append(f'<rect x="{cx-w/2:.1f}" y="{cy-h/2:.1f}" width="{w}" height="{h}" fill="{fill}" stroke="{C_LINE}" stroke-width="1"/>')
    rot = f' transform="rotate(-90 {cx:.1f} {cy:.1f})"' if vertical else ""
    out.append(f'<text x="{cx:.1f}" y="{cy+4:.1f}" font-size="11" font-weight="bold" fill="#1d2329" text-anchor="middle"{rot}>{escape(short)}</text>')
    if label:
        gap = BH / 2 + 10
        if side == 0:
            out.append(f'<text x="{cx-gap:.1f}" y="{cy+5:.1f}" font-size="14" font-weight="bold" fill="#1d2329" text-anchor="end">{escape(label)}</text>')
        elif side == 2:
            out.append(f'<text x="{cx+gap:.1f}" y="{cy+5:.1f}" font-size="14" font-weight="bold" fill="#1d2329">{escape(label)}</text>')
        elif side == 1:
            out.append(f'<text x="{cx+5:.1f}" y="{cy+gap:.1f}" font-size="14" font-weight="bold" fill="#1d2329" text-anchor="end" transform="rotate(-90 {cx+5:.1f} {cy+gap:.1f})">{escape(label)}</text>')
        else:
            out.append(f'<text x="{cx+5:.1f}" y="{cy-gap:.1f}" font-size="14" font-weight="bold" fill="#1d2329" transform="rotate(-90 {cx+5:.1f} {cy-gap:.1f})">{escape(label)}</text>')

out.append(f'<text x="{W/2}" y="{H-24}" font-size="15" fill="#59636d" text-anchor="middle">Drawn from BMS-Master.ioc and the CubeMX STM32G474R(B-C-E)Tx database. Green = assigned.</text>')
out.append("</svg>")
open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(out))
print("ok", OUT)
