import sys; input = sys.stdin.readline

N,M,K = map(int,input().split())

DP = [[-1]*M for _ in range(N+1)]
DP[1][0] = 0

graph = [[] for _ in range(N+1)]
for i in range(K):
    a,b,c = map(int,input().split())
    if a > b: continue
    graph[a].append((b,c))

for now in range(1,N+1):
    for nxt, cost in graph[now]:
        for i in range(1,M):
            if DP[now][i-1] == -1: continue
            DP[nxt][i] = max(DP[nxt][i], DP[now][i-1] + cost)

print(max(DP[-1]))