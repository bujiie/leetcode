#!/usr/bin/env python3

from sys import argv
from collections import defaultdict, Counter, deque
from re import match, search

filename = argv[1] if len(argv) > 1 else '0.in'

cases = []
with open(filename) as fp:
    for i, line in enumerate(fp):
        line = line.strip()

def solve(n):
    pass

for case in cases:
    print(solve(*case))