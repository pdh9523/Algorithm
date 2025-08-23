import sys; input = sys.stdin.readline
from collections import deque


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    x = find(a)
    y = find(b)
    
    if x != y:
        if rank[x] < rank[y]:
            parents[x] = y
        elif rank[x] > rank[y]:
            parents[y] = x
        else:
            parents[y] = x
            rank[x] += 1

def bfs(start, group):
    q = deque([start])
    visit = {start: 0}
    res = 0
    
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if nxt in group and nxt not in visit:
                visit[nxt] = visit[now] + 1
                res = max(res, visit[nxt])
                q.append(nxt)
    
    return res

N = int(input())
M = int(input())
parents = [*range(N+1)]
rank = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    union(a,b)

groups = dict()
for i in range(1, N+1): groups.setdefault(find(i), list()).append(i)

ans = []
for rep in groups:
    members = groups[rep]
    min_dst = float('inf')
    
    for member in members:
        dst = bfs(member, set(members))
        if dst < min_dst or (dst == min_dst and member < rep):
            min_dst = dst
            rep = member
    
    ans.append(rep)
    
ans.sort()
print(len(ans))
print(*ans, sep ="\n")