import sys; input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
arr = sorted([*map(int,input().split())] for _ in range(N))

hq = []
available = []
cnt = []
for s,e in arr:
    while hq and hq[0][0] < s:
        _, now = heappop(hq)
        heappush(available, now)

    if not available:
        cnt.append(1)
        heappush(hq, (e, len(cnt)))
    else:
        now = heappop(available)
        cnt[now-1] += 1
        heappush(hq, (e, now))

print(len(cnt))
print(*cnt)
