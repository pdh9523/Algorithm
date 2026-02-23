import sys; input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())

cur = int(input())
hq = []
for _ in range(N-1):
    heappush(hq, -int(input()))

ans = 0
while hq and cur <= -hq[0]:
    cur += 1
    ans += 1
    heappush(hq, heappop(hq) + 1)

print(ans)
