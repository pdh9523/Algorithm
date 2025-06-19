import sys; input = sys.stdin.readline
from heapq import heappop, heappush


N,D = map(int,input().split())

graph = [[] for _ in range(D+1)]
for i in range(D):
    graph[i].append((i+1, 1))

for _ in range(N):
    a,b,c = map(int,input().split())
    if b > D or a > D: continue
    graph[a].append((b,c))

hq = [(0,0)]
distance = [float('inf')] * (D+1)
distance[0] = 0
while hq:
    dist_now, now = heappop(hq)

    if dist_now > distance[now]: continue

    for nxt, cost in graph[now]:
        if distance[nxt] > dist_now + cost:
            distance[nxt] = dist_now + cost
            heappush(hq, (distance[nxt], nxt))

print(distance[D])