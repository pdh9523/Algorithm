import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def dijkstra(start, end, power):
    if start==end: return 0
    if (start,power) in dijk_cache: 
        return dijk_cache[(start,power)][end]
    
    distance = [float('inf')] * (V+1)
    distance[start] = 0
    hq = [(0,start)]
    while hq:
        dist_now, now = heappop(hq)

        if dist_now > distance[now]: continue

        for nxt, cost in graph[now]:
            if bogies[nxt] > power: continue
            if distance[nxt] > dist_now + cost:
                distance[nxt] = dist_now + cost
                heappush(hq, (distance[nxt], nxt))
    dijk_cache[(start,power)] = distance
    return distance[end]

def tsp(now=0, visit=1, power=0):
    if visit == (1<<(N+1))-1:
        return 0
    
    if (now, visit) in DP:
        return DP[(now, visit)]
    
    min_v = float('inf')
    for nxt in range(1, N+1):
        if visit & (1<<nxt): continue
        min_v = min(min_v, tsp(nxt, visit | (1<<nxt), power+1) + dijkstra(target[now], target[nxt], power))

    DP[(now, visit)] = min_v
    return min_v

N,V,E = map(int,input().split())
bogies = [0] + [*map(int,input().split())]
target = [1] + [*map(int,input().split())]

graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
dijk_cache = dict()
DP = dict()
ans = tsp()
print(ans if ans != float('inf') else -1)