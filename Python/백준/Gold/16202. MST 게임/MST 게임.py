import sys; input = sys.stdin.readline
from heapq import heappush, heappop


def mst():
    hq = [(0,1)]
    ans = 0
    visit = [False] * (N+1)
    visit[0] = True
    min_v = float('inf')
    s,e = -1,-1
    while hq:
        dist_now, now = heappop(hq)

        if visit[now]: continue
        visit[now] = True
        ans += dist_now

        for nxt,cost in graph[now]:
            if (now,nxt) in exclude: continue
            if cost < min_v:
                min_v = cost
                s,e = now,nxt
            heappush(hq, (cost,nxt))
    
    exclude.add((s,e))
    exclude.add((e,s))
    return ans if all(visit) else 0


N,M,K = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(1,M+1):
    a,b = map(int,input().split())
    graph[a].append((b,i))
    graph[b].append((a,i))

exclude = set()
ans = [0] * K 
for i in range(K):
    if (tmp:=mst()):
        ans[i] = tmp
    else: break
print(*ans)