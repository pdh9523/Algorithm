import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def dijkstra(distance, start, dist_start, ignore):
    hq = [(dist_start,start)]

    while hq:
        dist_now, now = heappop(hq)

        if dist_now > distance[now]: continue

        for nxt, cost in graph[now]:
            if nxt in ignore: continue
            dist_nxt = dist_now + cost
            if distance[nxt] > dist_nxt:
                distance[nxt] = dist_nxt
                heappush(hq, (dist_nxt, nxt))
    return distance

def trace_front(now,end):
    visit = set()
    while now != end:
        for nxt,cost in graph[now]:
            if distance[nxt] == distance[now]-cost:
                visit.add(nxt)
                now = nxt
                break
    return visit 
    

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
for g in graph: g.sort()

s,e = map(int,input().split())
# s -> e
distance = [float('inf')] * (N+1)
distance[e] = 0
distance = dijkstra(distance, e, 0, set())
# 시작을 역방향으로 해서 정방향 추적이 될 수 있도록 (간선은 양방향이니까 논리는 동일)
route = trace_front(s,e)
# e -> s
dist_start = distance[s]
distance = [float('inf')] * (N+1)
distance[e] = dist_start
distance = dijkstra(distance, e, dist_start, route)
print(distance[s])