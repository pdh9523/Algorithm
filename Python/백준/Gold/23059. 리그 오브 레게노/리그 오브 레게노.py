import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def topological_sort(arr):
    next_q = []
    q = deque(arr)
    while q:
        now = q.popleft()
        ans.append(now)
        if now not in graph: continue
        for nxt in graph[now]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                next_q.append(nxt)
    return sorted(next_q)

graph = dict()
in_degree = dict()
for _ in range(int(input())):
    a,b = input().split()
    graph.setdefault(a, list()).append(b)
    in_degree[b] = in_degree.get(b, 0)+1
    in_degree[a] = in_degree.get(a, 0)

q = sorted([i for i in in_degree if in_degree[i] == 0])

ans = []
while q:
    q = topological_sort(q)

print(-1 if any(in_degree.values()) else "\n".join(ans))