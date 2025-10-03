import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def dijkstra(start=1):
    hq = [(0,start)]
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    while hq:
        dist_now, now = heappop(hq)

        if dist_now > distance[now]: continue

        for nxt,cost in graph[now]:
            dist_nxt = dist_now + cost
            if distance[nxt] > dist_nxt:
                distance[nxt] = dist_nxt
                heappush(hq, (dist_nxt, nxt))

    return distance

N,M = map(int,input().split())
food = sorted([(x,i) for i,x in enumerate(map(int,input().split()),start=1) if x])
cafe = sorted([(x,i) for i,x in enumerate(map(int,input().split()),start=1) if x])


graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

distance = dijkstra()
ans = 0
for x,i in food:
    if distance[i] != float('inf'):
        ans = distance[i]
        distance_from_food = dijkstra(i)
        for y,j in cafe:
            if distance_from_food[j] != float('inf'):
                ans += distance_from_food[j]
                ans += distance[j]
                exit(print(ans))