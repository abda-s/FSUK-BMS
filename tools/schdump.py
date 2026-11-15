"""Dump components from an Altium .SchDoc without Altium.

Usage:
  python tools/schdump.py <SchDoc>            # components + parameters
  python tools/schdump.py <SchDoc> --text      # also net labels / ports / power ports

Why this exists: the Altium MCP server is not always attached to the session.
The .SchDoc is an OLE compound file; the 'FileHeader' stream holds every
record as pipe-separated key=value pairs. Properties are mixed case, so
everything is lower-cased. Text is ANSI (cp1252) unless prefixed with %UTF8%.
"""

import os
import sys

import olefile


def _fix(v):
    if v.startswith("%UTF8%"):
        try:
            return v[6:].encode("cp1252", errors="replace").decode("utf-8", errors="replace")
        except Exception:
            return v[6:]
    return v


def load(path):
    o = olefile.OleFileIO(path)
    raw = o.openstream("FileHeader").read().decode("cp1252", errors="replace")
    recs = []
    for chunk in raw.split("|RECORD=")[1:]:
        fields = chunk.split("|")
        kv = {"record": fields[0].strip()}
        for field in fields[1:]:
            if "=" in field:
                k, v = field.split("=", 1)
                # each value is NUL-terminated; what follows is binary padding
                kv[k.strip().lower()] = _fix(v.strip()).split("\x00")[0].strip()
        recs.append(kv)
    return recs


def components(recs):
    comps = []
    for r in recs:
        if r.get("record") == "1":
            comps.append({
                "designator": "",
                "params": {},
                "models": [],
                "lib": r.get("libreference", ""),
                "from": r.get("sourcelibraryname", ""),
                "desc": r.get("componentdescription", ""),
                "parts": r.get("partcount", ""),
                "partid": r.get("currentpartid", ""),
                "pins": [],
            })
    # OwnerIndex in the file is not a usable key. Designator records are
    # written in the same order as the component records: counts match and the
    # distinct parts line up on every sheet.
    desigs = [r.get("text", "") for r in recs
              if r.get("record") == "34" and r.get("name", "").lower() == "designator"]
    if len(desigs) == len(comps):
        for c, d in zip(comps, desigs):
            c["designator"] = d
    # Parameters, pins and implementation records belong to the last component seen.
    cur, pi = None, -1
    for r in recs:
        rt = r.get("record")
        if rt == "1":
            pi += 1
            cur = comps[pi]
            continue
        if cur is None:
            continue
        if rt == "41":
            cur["params"].setdefault(r.get("name", ""), r.get("text", ""))
        elif rt == "45":
            cur["models"].append(r.get("modelname", "") + " (" + r.get("modeltype", "") + ")")
        elif rt == "2":
            cur["pins"].append({
                "num": r.get("designator", ""),
                "name": r.get("name", ""),
                "x": r.get("location.x", ""),
                "y": r.get("location.y", ""),
                "len": r.get("pinlength", ""),
                "io": r.get("electrical", ""),
            })
    return comps


def labels(recs):
    out = []
    for r in recs:
        rt = r.get("record")
        if rt == "24":
            out.append(("netlabel", r.get("text", "")))
        elif rt == "22":
            out.append(("label", r.get("text", "")))
        elif rt == "38":
            out.append(("port", "%s io=%s style=%s" % (r.get("name", ""), r.get("iotype", ""), r.get("style", ""))))
        elif rt == "17":
            out.append(("powerport", r.get("text", "")))
        elif rt == "40":
            out.append(("sheetentry", r.get("name", "")))
        elif rt == "53":
            out.append(("harnessconn", r.get("text", "")))
        elif rt == "54":
            out.append(("harnessentry", r.get("text", "")))
        elif rt == "56":
            out.append(("signalharness", "%s verts" % r.get("locationcount", "")))
    return out


SHOW = ("value", "supplier part", "manufacturer part", "supplier footprint",
        "lcsc part name", "tolerance", "voltage rating", "resistance",
        "capacitance", "part number", "footprint", "package", "manufacturer")


if __name__ == "__main__":
    path = sys.argv[1]
    recs = load(path)
    print("##", os.path.basename(path))
    for c in components(recs):
        d = c["designator"] or "(unnamed)"
        print("-" * 95)
        print("%-9s %-30s from=%s" % (d, c["lib"][:30], c["from"] or "-"))
        if c["desc"]:
            print("          desc: %s" % c["desc"][:110])
        keys = [k for k in c["params"] if k.lower() in SHOW]
        for k in keys:
            print("          %s = %s" % (k, c["params"][k][:60]))
        extra = [k for k in c["params"]
                 if k.lower() not in SHOW and k.lower() not in ("comment", "designator", "currenttime", "currentdate")]
        if extra and "-v" in sys.argv:
            print("          other params: %s" % ", ".join(extra))
        if c["models"]:
            print("          models: %s" % c["models"])
    if "--text" in sys.argv:
        print("\n### LABELS / PORTS / HARNESSES")
        for kind, val in labels(recs):
            print("  %-14s %s" % (kind, val))
