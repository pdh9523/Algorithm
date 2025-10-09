import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def get_idx(cur):
    mn = float('inf')
    ret = -1
    for i in range(1, K - cur + 1):
        if hq[i] and hq[i][0] <= t and hq[i][0] < mn:
            mn = hq[i][0]
            ret = i
    return ret

N,P,K = map(int,input().split())

hq = [[] for _ in range(6)]
for _ in range(N):
    t,a = map(int,input().split())
    heappush(hq[a], t)

t = 0
answer = 0
while any(hq[i] for i in range(1, 6)):
    res = 0
    while True:
        idx = get_idx(res)
        if idx == -1:
            break
        res += idx
        answer += t - heappop(hq[idx])
    t += P

print(answer)
