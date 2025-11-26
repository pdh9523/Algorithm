import sys; input = sys.stdin.readline
from heapq import heappush, heappop


K,N,R = map(int, (input() for _ in range(3)))

graph = [[] for _ in range(N+1)]
for _ in range(R) :
    s,d,l,t = map(int,input().split())
    graph[s].append((d,l,t))

DP = [[float('inf')]*(K+1) for _ in range(N+1)]
DP[0][K] = 0

hq = [(0,K,1)]

ans = float('inf')
while hq:
    dist_now, cost_now, now = heappop(hq)
    if now == N:
        ans = min(ans, dist_now)
        break

    for nxt, dist_nxt, cost_nxt in graph[now]:
        if (cost:=cost_now-cost_nxt) < 0: continue
        if DP[nxt][cost] > dist_now + dist_nxt:
            DP[nxt][cost] = dist_now + dist_nxt
            heappush(hq, (dist_now+dist_nxt, cost, nxt))

print(ans if ans < float('inf') else -1)