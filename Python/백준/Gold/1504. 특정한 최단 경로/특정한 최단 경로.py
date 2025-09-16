import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def dijkstra(start,end):
    hq = [(0,start)]
    distance = [float('inf')] * (N+1)
    distance[start] = 0

    while hq :
        dist_now, now = heappop(hq)
        if distance[now] >= dist_now :
            for next, dist_next in graph[now]:
                cost = dist_now + dist_next
                if distance[next] > cost:
                    distance[next] = cost
                    heappush(hq,((cost,next)))
    return distance[end]

N,E = map(int,input().split())
graph = [ [] for _ in range(N+1)]

for _ in range(E) :
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

v1,v2 = map(int,input().split())

tmp1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,N)
tmp2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,N)
if min(tmp1,tmp2) == float('inf') :
    print(-1)
else :
    print(min(tmp1,tmp2))