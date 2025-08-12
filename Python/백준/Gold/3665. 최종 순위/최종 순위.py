import sys; input = sys.stdin.readline
from collections import deque


def solve():
    N = int(input())
    graph = [set() for _ in range(N+1)]
    in_degree = [0] * (N+1)

    arr = [*map(int,input().split())]
    for i in range(N):
        for j in range(i+1, N):
            graph[arr[i]].add(arr[j])
            in_degree[arr[j]] += 1
    
    for _ in range(int(input())):
        a,b = map(int,input().split())
        if b in graph[a]:
            graph[a].discard(b)
            in_degree[b] -= 1
            graph[b].add(a)
            in_degree[a] += 1
        else:
            graph[b].discard(a)
            in_degree[a] -= 1
            graph[a].add(b)
            in_degree[b] += 1
    ans = []
    q = deque([x for x in range(1,N+1) if in_degree[x] == 0])
    while q:
        now = q.popleft()
        ans.append(now)
        for nxt in graph[now]:
            in_degree[nxt] -= 1

            if in_degree[nxt] == 0:
                q.append(nxt)
    
    if len(ans) != N:
        return print("IMPOSSIBLE")
    else:
        return print(" ".join(map(str, ans)))

for _ in range(int(input())): solve()