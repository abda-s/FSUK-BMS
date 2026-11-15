"""Build a netlist from an Altium .SchDoc without Altium.

Objects are joined where they physically touch:
  * wire polyline (RECORD=27) endpoints / a point on another wire
  * pin hotspot = pin Location + PinLength in one of four directions
    (direction is not a separate key here; the one that lands on copper wins)
  * net label (25), port (18), power port (17) sitting on a wire or exactly on
    a pin hotspot
Nets carrying the same label name are merged (as Altium does).

Usage: python tools/schnetlist.py <SchDoc> [--noerc]
"""
import re
import sys

from schdump import components, load

TOL = 3


def num(rec, key):
    v = (rec.get(key, "0") or "0").strip()
    m = re.match(r"^[-+]?\d+(?:\.\d+)?", v)
    f = float(m.group(0)) if m else 0.0
    frac = (rec.get(key + "_frac", "") or "").strip()
    m = re.match(r"^[-+]?\d+(?:\.\d+)?", frac) if frac else None
    if m:
        f += float(m.group(0)) / 1e5 * (1 if f >= 0 else -1)
    return f


def point(rec):
    return (round(num(rec, "location.x"), 4), round(num(rec, "location.y"), 4))


def on_segment(p, a, b, tol=TOL):
    px, py = p
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return abs(px - ax) <= tol and abs(py - ay) <= tol
    cross = dx * (py - ay) - dy * (px - ax)
    if abs(cross) > tol * ((dx * dx + dy * dy) ** 0.5):
        return False
    dot = (px - ax) * dx + (py - ay) * dy
    return -tol <= dot <= dx * dx + dy * dy + tol


class DSU:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra


def build(recs):
    dsu = DSU()
    segs, pins, labels, noerc = [], [], [], []
    comp_list = components(recs)
    ci = -1
    cur = None
    for r in recs:
        rt = r.get("record")
        if rt == "1":
            ci += 1
            cur = comp_list[ci]
        elif rt == "27":
            n = int(num(r, "locationcount"))
            pts = [(round(num(r, "x%d" % (i + 1)), 4), round(num(r, "y%d" % (i + 1)), 4))
                   for i in range(n)]
            for i in range(n - 1):
                segs.append(("w%d" % len(segs), pts[i], pts[i + 1]))
                dsu.find("w%d" % (len(segs) - 1))
        elif rt == "2":
            pins.append({"key": "p%d" % len(pins), "p": point(r), "num": r.get("designator", ""),
                         "name": r.get("name", ""), "len": num(r, "pinlength"), "comp": cur})
        elif rt in ("25", "18", "17"):
            kind = {"25": "netlabel", "18": "port", "17": "power"}[rt]
            text = r.get("text", "") if rt != "18" else r.get("name", "")
            labels.append({"key": "l%d" % len(labels), "p": point(r), "text": text, "kind": kind,
                           "w": num(r, "width")})
        elif rt == "22":
            noerc.append(point(r))

    for i in range(len(segs)):
        sid, a, b = segs[i]
        for j in range(i + 1, len(segs)):
            _, c, d = segs[j]
            if a == c or a == d or b == c or b == d:
                dsu.union(sid, segs[j][0])
            elif on_segment(a, c, d) or on_segment(b, c, d) or on_segment(c, a, b) or on_segment(d, a, b):
                dsu.union(sid, segs[j][0])

    def wire_at(p):
        for sid, a, b in segs:
            if a == p or b == p or on_segment(p, a, b):
                return dsu.find(sid)
        return None

    unresolved_pins, unresolved_labels = [], []
    label_pts = {}
    for lb in labels:
        label_pts.setdefault(lb["p"], []).append(lb)
    for pin in pins:
        dsu.find(pin["key"])
        cands = [(round(pin["p"][0] + dx * pin["len"], 4),
                  round(pin["p"][1] + dy * pin["len"], 4))
                 for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1))]
        hit = None
        for q in cands + [pin["p"]]:
            w = wire_at(q)
            if w is not None:
                hit = w
                pin["hot"] = q
                break
        if hit is None:
            # a power port / label can sit straight on the pin hotspot
            for q in cands:
                if q in label_pts:
                    pin["hot"] = q
                    for lb in label_pts[q]:
                        dsu.union(pin["key"], lb["key"])
                    break
        if hit is None:
            if "hot" not in pin:
                pin["hot"] = pin["p"]
                unresolved_pins.append(pin)
            continue
        dsu.union(hit, pin["key"])
    for lb in labels:
        dsu.find(lb["key"])
        w = wire_at(lb["p"])
        if w is None and lb["kind"] == "port" and lb["w"]:
            # a port's anchor is at one end of its body; try the other end too
            for dx in (lb["w"], -lb["w"]):
                q = (round(lb["p"][0] + dx, 4), lb["p"][1])
                w = wire_at(q)
                if w is not None:
                    lb["p"] = q
                    break
        if w is not None:
            dsu.union(w, lb["key"])
        else:
            unresolved_labels.append(lb)

    # labels directly on a pin hotspot
    for lb in list(unresolved_labels):
        for pin in pins:
            if pin.get("hot") == lb["p"]:
                dsu.union(pin["key"], lb["key"])
                unresolved_labels.remove(lb)
                break

    groups = {}
    for pin in pins:
        if pin in unresolved_pins:
            continue
        g = groups.setdefault(dsu.find(pin["key"]), {"pins": [], "names": set()})
        g["pins"].append((pin["comp"]["designator"], pin["num"], pin["name"]))
    for lb in labels:
        g = groups.setdefault(dsu.find(lb["key"]), {"pins": [], "names": set()})
        if lb["text"]:
            g["names"].add(lb["text"])

    # merge by label name
    by_name = {}
    for k, g in groups.items():
        for n in g["names"]:
            by_name.setdefault(n, []).append(k)
    nr = DSU()
    for n, ks in by_name.items():
        for k in ks[1:]:
            nr.union(ks[0], k)
    merged = {}
    for k, g in groups.items():
        mk = nr.find(k)
        m = merged.setdefault(mk, {"pins": [], "names": set()})
        m["pins"] += g["pins"]
        m["names"] |= g["names"]
    return merged, segs, pins, labels, unresolved_pins, noerc


if __name__ == "__main__":
    path = sys.argv[1]
    nets, segs, pins, labels, unresolved, noerc = build(load(path))
    rows = []
    for k, v in nets.items():
        name = "|".join(sorted(n for n in v["names"] if n)) or "(unnamed)"
        rows.append((name, ", ".join("%s.%s(%s)" % p for p in sorted(set(v["pins"])))))
    for name, ps in sorted(rows):
        print("%-24s %s" % (name[:24], ps))
    print("\n%d wires, %d pins, %d labels, %d nets" % (len(segs), len(pins), len(labels), len(nets)))
    if unresolved:
        print("pins on no wire and no label: %d" % len(unresolved))
        for u in unresolved:
            mark = " [no-ERC at %s]" % (u["p"],) if any(
                abs(u["p"][0] - n[0]) <= 10 and abs(u["p"][1] - n[1]) <= 10 for n in noerc) else ""
            print("   %s pin %s (%s) at %s%s" % (u["comp"]["designator"], u["num"], u["name"], u["p"], mark))
