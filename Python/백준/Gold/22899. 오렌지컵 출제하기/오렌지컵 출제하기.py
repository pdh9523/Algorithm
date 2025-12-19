import sys; input = lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush


N,K = map(int,input().split())

hq = []

data = dict()
for idx, t in zip(map(int,input().split()), map(int,input().split())):
    data.setdefault(idx, list()).append(t)

for k in data:
    data[k].sort()

    for i in range(len(data[k])):
        heappush(hq, (i, data[k][i]))

ans = [-1] * N
tmp = []
now = 0
for i in range(N):
    while hq and hq[0][0] <= i:
        _, t = heappop(hq)
        now += t
        heappush(tmp, -t)
    
    if len(tmp) < K:
        continue

    while len(tmp) > K:
        now += heappop(tmp)
    
    ans[i] = now

print(*ans)
