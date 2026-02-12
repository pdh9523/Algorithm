import sys; input = sys.stdin.readline
from heapq import heappop, heappush

def get_rushed_cost(current_time, length, S, E):
    remaining = length
    elapsed = 0
    t = current_time

    if t < S:
        time_before_rush = S - t
        if remaining <= time_before_rush:
            return remaining
        remaining -= time_before_rush
        elapsed += time_before_rush
        t = S

    if t < E:
        rush_time_left = E - t

        distance_in_rush = rush_time_left / 2
        if remaining <= distance_in_rush:
            return elapsed + remaining * 2
        remaining -= distance_in_rush
        elapsed += rush_time_left

    elapsed += remaining
    return elapsed

start = 1

N,M,S,E = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c,r1,r2 = map(int,input().split())
    graph[a].append((b,c,r1))
    graph[b].append((a,c,r2))

distance = [float('inf')] * (N+1)
distance[start] = 0
hq = [(0,start)]
while hq:
    dist_now, now = heappop(hq)

    if dist_now > distance[now]: continue

    for nxt, cost, rush in graph[now]:
        if rush:
            cost = get_rushed_cost(dist_now, cost, S, E)

        if distance[nxt] > dist_now + cost:
            distance[nxt] = dist_now + cost
            heappush(hq, (distance[nxt], nxt))

ans = max(distance[1:])
if ans % 1 == 0:
    ans = int(ans)
print(ans)
