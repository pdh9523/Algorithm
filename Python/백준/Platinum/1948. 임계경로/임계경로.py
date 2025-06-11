import sys; input = sys.stdin.readline
from collections import deque


N = int(input())
M = int(input())

in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
cnt = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    in_degree[b] += 1
start, end = map(int,input().split())

q = deque([start])
visit = [0] * (N+1)
while q:
    now = q.popleft()
    for nxt,cost in graph[now]:
        in_degree[nxt] -= 1
    
        if visit[nxt] < visit[now] + cost:
            visit[nxt] = visit[now] + cost
            cnt[nxt] = [now]
        elif visit[nxt] == visit[now] + cost:
            cnt[nxt].append(now)
        
        if in_degree[nxt] == 0:
            q.append(nxt)

q = deque([end])
route = set()
while q:
    now = q.popleft()
    for x in cnt[now]:
        if (now,x) not in route:
            route.add((now,x))
            q.append(x)

print(visit[end])
print(len(route))