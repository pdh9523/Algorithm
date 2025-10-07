import sys; input = lambda: sys.stdin.readline().rstrip()


def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        parents[a] = b

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def kruskal():
    cnt = 0 
    res = 0
    for a,b,c in edges:
        if find(a) == find(b): continue
        graph[a].append((b,c))
        graph[b].append((a,c))
        union(a,b)
        cnt += 1
        res += c
        if cnt == N-1:
            return res

def dfs(now, visit=0, dist=0):
    global max_v
    if visit & (1<<now): return
    max_v = max(max_v, dist)
    visit |= 1<<now

    for nxt,cost in graph[now]:
        dfs(nxt, visit, dist+cost)

N,K = map(int,input().split())
parents = [*range(N)]
edges = sorted([[*map(int,input().split())] for _ in range(K)],key=lambda x:x[2])
graph = [[] for _ in range(N)]

print(kruskal())
max_v = 0
for start in range(N):
    dfs(start)
print(max_v)
