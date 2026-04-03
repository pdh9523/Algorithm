import sys; input = sys.stdin.readline
from heapq import heappop, heappush

def solve():
    N,M = map(int,input().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))

    S,F = map(int,input().split())

    distance = [float('inf')]*(N+1)
    distance[S] = 0
    hq = [(0,S)]

    while hq:
        dist_now, now = heappop(hq)
        if dist_now > distance[now]: continue
        for nxt,cost in graph[now]:
            dist_nxt = dist_now + cost
            if dist_nxt < distance[nxt]:
                distance[nxt] = dist_nxt
                heappush(hq, (dist_nxt, nxt))

    target = distance[F]

    cnt = [[0,0] for _ in range(N+1)]
    cnt[S][0] = 1
    processed = [[False,False] for _ in range(N+1)]
    hq = [(0,S,0)]

    while hq:
        dist_now, now, t = heappop(hq)
        if processed[now][t]: continue
        processed[now][t] = True

        for nxt,cost in graph[now]:
            dist_nxt = dist_now + cost
            if dist_nxt > target + 1: continue

            nt = dist_nxt - distance[nxt]
            if nt < 0 or nt > 1 or processed[nxt][nt]: continue

            cnt[nxt][nt] += cnt[now][t]
            heappush(hq, (dist_nxt, nxt, nt))

    print(sum(cnt[F]))

for _ in range(int(input())):
    solve()
