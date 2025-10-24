import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)


def dfs(now, target, max_v=0, res=0):
    if now == target:
        exit(print(res-max_v))
    
    visit[now] = True
    for nxt, cost in graph[now]:
        if visit[nxt]: continue
        dfs(nxt, target, max(max_v, cost), res+cost)

N,A,B = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
visit = [False] * (N+1)
dfs(A,B)