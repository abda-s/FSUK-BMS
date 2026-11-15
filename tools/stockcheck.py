"""Check JLCPCB/LCSC SMT stock for every distinct LCSC part in the BOM.

Reads the LCSC codes straight out of the .SchDoc files (via schdump.py, no
Altium needed), then queries the JLCPCB SMT parts API for each code and prints
a table with stock, price and a LOW/OUT flag.

Usage:  python tools/stockcheck.py
"""
import glob
import json
import os
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from schdump import components, load

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHEETS = glob.glob(os.path.join(REPO, "BMS-Master", "Sheets", "*.SchDoc"))

API = "https://jlcpcb.com/api/overseas-pcb-order/v1/shoppingCart/smtGood/selectSmtComponentList"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
}


def query(code):
    body = json.dumps({"currentPage": 1, "pageSize": 5, "keyword": code}).encode("utf-8")
    req = urllib.request.Request(API, data=body, headers=HEADERS, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8", errors="replace"))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, OSError) as e:
        return {"_error": str(e)}


def main():
    # Collect every part, keyed by LCSC code (designators + first mpn/value/desc).
    parts = defaultdict(lambda: {"refs": [], "mpn": "", "value": "", "desc": ""})
    for path in sorted(SHEETS):
        for c in components(load(path)):
            p = c["params"]
            code = p.get("Supplier Part", "").strip()
            if not code:
                continue
            parts[code]["refs"].append(c["designator"])
            if not parts[code]["mpn"]:
                parts[code]["mpn"] = (p.get("Manufacturer Part", "") or p.get("Part Number", "")).strip()
            if not parts[code]["value"]:
                parts[code]["value"] = (p.get("Value", "") or p.get("value", "")).strip()
            if not parts[code]["desc"]:
                parts[code]["desc"] = (c.get("desc", "") or "").strip()

    codes = sorted(parts)
    print("Checking %d distinct LCSC parts..." % len(codes))
    print()

    hdr = "%-10s %-22s %-30s %8s %8s  %s" % (
        "LCSC", "MPN", "value / description", "stock", "price", "flag")
    print(hdr)
    print("-" * len(hdr))

    rows = []
    for i, code in enumerate(codes):
        info = parts[code]
        refs = " ".join(info["refs"])
        res = query(code)

        if "_error" in res:
            rows.append((code, info, None, res["_error"], refs))
            continue

        # Find the exact componentCode match in the returned list.
        stock = None
        price = None
        model = ""
        describe = ""
        try:
            lst = res["data"]["componentPageInfo"]["list"]
        except (KeyError, TypeError):
            lst = []
        for item in lst:
            if str(item.get("componentCode", "")) == code:
                stock = item.get("stockCount")
                price = item.get("initialPrice")
                model = item.get("componentModelEn", "")
                describe = item.get("describe", "")
                break

        if stock is None:
            rows.append((code, info, None, "not found in SMT list", refs))
        else:
            rows.append((code, info, (stock, price, model, describe), None, refs))

        if i < len(codes) - 1:
            time.sleep(0.4)

    for code, info, found, err, refs in rows:
        mpn = info["mpn"] or "-"
        valdesc = info["value"] or (info["desc"][:30] if info["desc"] else "-")
        if found is None:
            # error or not found
            print("%-10s %-22s %-30s %8s %8s  %s" % (code, mpn, valdesc, "-", "-", err or "?"))
            continue
        stock, price, model, describe = found
        if model and model not in mpn:
            mpn = model
        flag = "OUT" if stock == 0 else ("LOW" if stock < 100 else "")
        pstr = ("%.4f" % price) if isinstance(price, (int, float)) else (price or "-")
        print("%-10s %-22s %-30s %8s %8s  %s" % (code, mpn, valdesc, stock, pstr, flag))

    print()
    print("LOW = stock < 100, OUT = stock == 0. Parts not found: check LCSC manually.")
    print("refs per part: use `python tools/bomcheck.py`.")


if __name__ == "__main__":
    main()
