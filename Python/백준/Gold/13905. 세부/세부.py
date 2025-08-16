import sys; input = sys.stdin.readline
from heapq import heappop, heappush


N,M = map(int,input().split())
start,end = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance = [0] * (N+1)
distance[0] = float('inf')

hq = [(-float('inf'), start)]
while hq:
    dist_now, now = heappop(hq)
    dist_now *= -1
    if distance[now] > dist_now: continue

    for nxt, cost in graph[now]:
        dist_nxt = min(dist_now, cost)
        if dist_nxt > distance[nxt]:
            distance[nxt] = dist_nxt
            heappush(hq, (-dist_nxt, nxt))

print(distance[end])