import sys; input = sys.stdin.readline
from collections import deque


N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

start,end = map(int,input().split())

q = deque([start])
visit = [0] * (N+1)
data = dict()
while q:
    now = q.popleft()
    for nxt in sorted(graph[now]):
        if not visit[nxt]:
            visit[nxt] = visit[now] + 1
            data[nxt] = data.setdefault(now, set()) | {now}
            q.append(nxt)

q = deque([end])
rev_visit = [0] * (N+1)
check_point = data[end] - {start}
while q:
    now = q.popleft()

    for nxt in graph[now]:
        if not rev_visit[nxt] and nxt not in check_point:
            rev_visit[nxt] = rev_visit[now] + 1
            q.append(nxt)

print(visit[end] + rev_visit[start])