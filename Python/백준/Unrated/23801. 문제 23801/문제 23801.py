import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def dijkstra(graph, start):
    hq = [(0, start)]
    distance = [float('inf')] * len(graph)
    distance[start] = 0
    
    while hq:
        dist_now, now = heappop(hq)
        if dist_now > distance[now]: continue

        for nxt, cost in graph[now]:
            if distance[nxt] > dist_now + cost:
                distance[nxt] = dist_now + cost
                heappush(hq, (dist_now + cost, nxt))
                
    return distance

N,M = map(int,input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start, end = map(int,input().split())

input()
points = [*(map(int,input().split()))]

dist_start = dijkstra(graph, start)
dist_end = dijkstra(graph, end)

ans = float('inf')
for p in points:
    ans = min(ans, dist_start[p] + dist_end[p])

print(ans if ans != float('inf') else -1)
