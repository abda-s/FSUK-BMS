"""BOM analysis for the BMS-Master schematic (no Altium needed).

Extracts every component from the .SchDoc files, then reports:
  1. per-LCSC-part usage (refs) and any value inconsistencies within a part
  2. the same value+package appearing under multiple LCSC parts (consolidation)
  3. parts with no LCSC number

Usage:  python tools/bomcheck.py
"""
import glob
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from schdump import components, load

SHEETS = glob.glob(r"E:\Documents\Racing\FSUK-BMS\BMS-Master\Sheets\*.SchDoc")

# Map RKM-style values (4K7, 100n, 2u2, 60R4, 0R) and plain values to a
# canonical form for comparison.
RKM = {
    "R": 1, "K": 1e3, "M": 1e6,
    "p": 1e-12, "n": 1e-9, "u": 1e-6, "m": 1e-3,
}


def canon_value(v):
    v = (v or "").strip()
    if not v:
        return None
    v = v.replace(" ", "")
    # strip leading units like "F", "R" that are part of RKM notation handled below
    # handle 4K7 / 100n / 60R4 / 2u2 / 0R / 0 / 10K / 330R / 49R9
    m = re.fullmatch(r"(\d+(?:\.\d+)?)([RKM])?(\d+)?", v)
    if not m:
        return v  # non-numeric (e.g. "100n" handled below)
    return v  # fall through; canonicalization below is best-effort


def norm(v):
    """Best-effort numeric canonical value, else the string."""
    s = (v or "").strip().replace(" ", "").replace(",", ".")
    if s in ("", "0", "0R", "0R0"):
        return 0.0
    # 4K7 / 60R4 / 2u2 / 49R9 (digit, unit-letter, digit)
    m = re.fullmatch(r"(\d+(?:\.\d+)?)([RKM])(\d+(?:\.\d+)?)", s)
    if m:
        a, unit, b = m.group(1), m.group(2), m.group(3)
        return float(a + "." + b) * RKM[unit]
    # 100n / 10p / 2u2 (digits + unit suffix)
    m = re.fullmatch(r"(\d+(?:\.\d+)?)([pnumk])(?:[F]?)", s)
    if m:
        return float(m.group(1)) * RKM[m.group(2)]
    # 10K / 330R / 1K / 100M (digits + R/K/M)
    m = re.fullmatch(r"(\d+(?:\.\d+)?)([RKM])", s)
    if m:
        return float(m.group(1)) * RKM[m.group(2)]
    # plain number
    m = re.fullmatch(r"(\d+(?:\.\d+)?)", s)
    if m:
        return float(m.group(1))
    return s


def main():
    rows = []
    for path in sorted(SHEETS):
        sheet = os.path.basename(path).replace(".SchDoc", "")
        for c in components(load(path)):
            p = c["params"]
            lcsc = p.get("Supplier Part", "")
            rows.append({
                "sheet": sheet,
                "ref": c["designator"],
                "lib": c["lib"],
                "lcsc": lcsc,
                "mpn": p.get("Manufacturer Part", "") or p.get("Part Number", ""),
                "value": p.get("Value", "") or p.get("value", ""),
                "desc": c["desc"],
            })

    refs = [r for r in rows if r["ref"]]

    # duplicates of designator
    seen = {}
    for r in refs:
        seen.setdefault(r["ref"], []).append(r["sheet"])
    dups = {k: v for k, v in seen.items() if len(v) > 1}

    print("=== BOM (%d components) ===" % len(refs))
    print()

    # 1) per LCSC part
    by_lcsc = defaultdict(list)
    for r in refs:
        by_lcsc[r["lcsc"]].append(r)
    print("### Parts with multiple instances (same LCSC)")
    print("%-10s %-6s %s" % ("LCSC", "qty", "refs"))
    for lcsc, lst in sorted(by_lcsc.items(), key=lambda kv: -len(kv[1])):
        if not lcsc:
            continue
        vals = {norm(x["value"]) for x in lst if x["value"]}
        flag = ""
        if len(vals) > 1:
            flag = "  <-- VALUE MISMATCH: " + str(sorted(vals, key=str))
        print("%-10s %-6d %s%s" % (lcsc, len(lst), " ".join(x["ref"] for x in lst), flag))

    print()
    print("### Same value+package but DIFFERENT LCSC parts (consolidate?)")
    # value only (package not reliably parsed here)
    by_val = defaultdict(set)
    for r in refs:
        n = norm(r["value"])
        if n is not None and r["lcsc"]:
            by_val[(n, r["lib"][:6])].add((r["lcsc"], r["mpn"]))
    for (val, lib), parts in sorted(by_val.items(), key=lambda kv: str(kv[0])):
        if len(parts) > 1:
            print("  value=%s (%s):" % (val, lib))
            for lcsc, mpn in sorted(parts):
                print("      %s  %s" % (lcsc, mpn))

    print()
    print("### No LCSC part number")
    for r in refs:
        if not r["lcsc"]:
            print("  %-6s %-16s %s" % (r["ref"], r["sheet"], r["lib"]))

    print()
    print("### Duplicate designators (should be empty)")
    for k, v in dups.items():
        print("  %s appears on %s" % (k, v))

    # write CSV for stock check
    out = os.path.join(os.path.dirname(__file__), "_bom_lcsc.csv")
    with open(out, "w", newline="", encoding="utf-8-sig") as f:
        f.write("lcsc,mpn,value,refs\n")
        for lcsc, lst in sorted(by_lcsc.items()):
            if not lcsc:
                continue
            mpn = lst[0]["mpn"]
            val = lst[0]["value"]
            f.write("%s,%s,%s,%s\n" % (lcsc, mpn.replace(",", ";"), val.replace(",", ";"),
                                       " ".join(x["ref"] for x in lst)))
    print("\nWrote tools/_bom_lcsc.csv (LCSC -> refs) for the stock check.")


if __name__ == "__main__":
    main()
