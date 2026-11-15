"""Compare two schnetlist outputs: per designator, the SET of nets it touches.

Ignores pin numbers (resistors are symmetric). Usage:
  python netcmp.py before.txt after.txt
"""
import re
import sys
from collections import defaultdict


def parse(path):
    d = defaultdict(set)  # designator -> set of nets
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^(\S.*?)\s{2,}(.*)$", line.rstrip())
        if not m:
            continue
        net = m.group(1).strip()
        body = m.group(2)
        for ref, num in re.findall(r"([A-Z]+\d+)\.(\d+)", body):
            d[ref].add(net)
    return d


a = parse(sys.argv[1])
b = parse(sys.argv[2])
refs = sorted(set(a) | set(b))
bad = 0
for r in refs:
    if a.get(r) != b.get(r):
        bad += 1
        print("DIFF %-6s before=%s after=%s" % (r, sorted(a.get(r, set())), sorted(b.get(r, set()))))
print("checked %d designators, %d differ" % (len(refs), bad))
