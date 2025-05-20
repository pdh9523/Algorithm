import sys; input = sys.stdin.readline
from heapq import heappop, heappush


hq = []
for _ in range(int(input())):
    heappush(hq, -int(input()))

    if len(hq) > 4: heappop(hq)

res = []
for x in range(len(hq)):
    for y in range(len(hq)):
        if x==y: continue
        res.append(int(str(-hq[x])+str(-hq[y])))
print(sorted(res)[2])
