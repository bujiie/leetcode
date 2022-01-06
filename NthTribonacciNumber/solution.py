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

def solve_down(n):
    def dp(i):
        if i == 0:
            return 0
        if i < 3:
            return 1
        if i not in mem:
            mem[i] = sum([dp(i-j) for j in range(1,4)])
        return mem[i]
                
    mem = {}
    return dp(n)

def solve_up(n):
    if n == 0:
        return 0
    if n < 3:
        return 1

    mem = [0] * (n+1)
    mem[0], mem[1], mem[2] = 0, 1, 1
    for i in range(3, n+1):
        mem[i] = sum([mem[i-j] for j in range(1,4)])
    return mem[-1]

def solve_borrowed(n):
    a, b, c = 1, 0, 0
    for _ in range(n): a, b, c = b, c, a + b + c
    return c


for case in cases:
    print(solve_borrowed(case))
