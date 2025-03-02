import sys; input = sys.stdin.readline; sys.setrecursionlimit(50001)
from math import ceil, log2


def dfs(now=1, d=0):
    depth[now] = d
    visit[now] = True

    for nxt in graph[now]:
        if visit[nxt]: continue
        parent[nxt][0] = now
        dfs(nxt, d+1)

def build_sparse_table():
    for j in range(1, LOG):
        for i in range(1, N+1):
            if parent[i][j-1]: 
                parent[i][j] = parent[parent[i][j-1]][j-1] # 직전 부모가 있다면, 그쪽으

def lca(a,b):
    if depth[a] < depth[b]:
        a,b = b,a
    
    diff = depth[a] - depth[b]
    for i in range(LOG):
        if diff & ( 1<<i ):
            a = parent[a][i]
    
    if a == b:
        return a
    
    for i in range(LOG-1,-1,-1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    
    return parent[a][0]


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

LOG = ceil(log2(N))

visit = [False] * (N+1)
parent = [[0] * LOG for _ in range(N+1)]
depth = [0] * (N+1)

dfs()
build_sparse_table()

M = int(input())
for _ in range(M):
    print(lca(*map(int,input().split())))