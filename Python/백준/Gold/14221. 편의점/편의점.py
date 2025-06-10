import sys; input = sys.stdin.readline
from heapq import heappop, heappush


N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance = [float('inf')] * (N+1)
K,L = map(int,input().split())
ends = [*map(int,input().split())]
starts = [*map(int,input().split())]

for start in starts:
    distance[start] = 0
hq = [(0, start) for start in starts]

while hq:
    dist_now, now = heappop(hq)

    if dist_now > distance[now]: continue

    for nxt,cost in graph[now]:
        if distance[nxt] > dist_now + cost:
            distance[nxt] = dist_now + cost
            heappush(hq, (distance[nxt], nxt))

ans = -1
dist = float('inf')
for end in sorted(ends):
    if dist > distance[end]:
        dist = distance[end]
        ans = end

print(ans)