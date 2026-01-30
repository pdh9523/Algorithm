import sys; input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
arr = sorted([*map(int,input().split())] for _ in range(N))

hq = []
available = []
count = [0]
max_v = 0
for s,e in arr:
    while hq and hq[0][0] < s:
        _, now = heappop(hq)
        heappush(available, now)

    if not available:
        max_v += 1
        count.append(1)
        heappush(hq, (e, max_v))
    else:
        now = heappop(available)
        count[now] += 1
        heappush(hq, (e, now))

print(max_v)
print(*count[1:])
