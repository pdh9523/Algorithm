import sys; input = sys.stdin.readline
from heapq import heappop, heappush

start = 1

def dijkstra(graph, shortcut):
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    hq = [(0, start)]

    while hq:
        dist_now, now = heappop(hq)

        if dist_now > distance[now]: continue

        for nxt, cost in shortcut[now]:
            if distance[nxt] > (tmp:=max(distance[now], K)) + cost:
                distance[nxt] = tmp + cost
                heappush(hq, (distance[nxt], nxt))
        
        for nxt, cost in graph[now]:
            if distance[nxt] > distance[now] + cost:
                distance[nxt] = distance[now] + cost
                heappush(hq, (distance[nxt], nxt))
        
    return distance[-1]

N,K,X,Y = map(int,input().split())

graph = [[] for _ in range(N+1)]
shortcut = [[] for _ in range(N+1)]

for _ in range(X):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for _ in range(Y):
    a,b,c = map(int,input().split())
    shortcut[a].append((b,c))
    shortcut[b].append((a,c))

print(dijkstra(graph, shortcut))
