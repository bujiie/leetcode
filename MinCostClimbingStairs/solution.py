#!/usr/bin/env python3

from sys import argv
from collections import defaultdict, Counter, deque
from re import match, search

filename = argv[1] if len(argv) > 1 else '0.in'

cases = []
with open(filename) as fp:
    for i, line in enumerate(fp):
        line = line.strip()
        cases.append([int(n) for n in line.split(',')])


def solve(cost):
    if len(cost) == 1:
        return cost[0]

    # the last index is not considered the top in this problem.
    # we fudge an imaginary top stair with cost 0.
    cost += [0]

    # initialize list so we can access by index.
    dp = [0] * len(cost)

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, len(cost)):
        dp[i] = min(dp[i-1], dp[i-2])+cost[i]
    return dp[-1]


for case in cases:
    print(solve(case))
