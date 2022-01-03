#!/usr/bin/env python3

from sys import argv
from collections import defaultdict, Counter, deque
from re import match, search

filename = argv[1] if len(argv) > 1 else '0.in'

cases = []
with open(filename) as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        cases.append(int(line))

S = {0:0, 1:1}
def solve(n):
    if n < 2:
        return n
    if n not in S:
        S[n] = solve(n-1) + solve(n-2)
    return S[n]

for case in cases:
    print(solve(case))
