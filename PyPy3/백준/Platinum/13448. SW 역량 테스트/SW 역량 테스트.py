import sys; input = sys.stdin.readline
from functools import cmp_to_key


def cmp(a,b):
    ap, ar = a[1], a[2]
    bp, br = b[1], b[2]
    if ap * br > bp * ar:
        return -1
    elif ap * br < bp * ar:
        return 1
    return 0

N,T = map(int,input().split())
arr = sorted([x for x in zip(map(int,input().split()), map(int,input().split()), map(int,input().split()))], key=cmp_to_key(cmp))

DP = [0] * (T+1)
for m,p,r in arr:
    for t in range(T, -1, -1):
        if t-r < 0: continue
        DP[t] = max(DP[t], DP[t-r] + (m-(t*p)))

print(max(DP))