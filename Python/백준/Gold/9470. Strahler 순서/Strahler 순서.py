import sys; input = sys.stdin.readline
from collections import deque


def solve():
    T,N,K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    in_degree = [0] * (N+1)
    strahler = [[] for _ in range(N+1)]

    for _ in range(K):
        a,b = map(int,input().split())
        graph[a].append(b)
        in_degree[b] += 1
    
    q = deque()
    for i in range(1, N+1):
        if in_degree[i]==0:
            q.append(i)
            strahler[i] = [1, 0]
    
    while q:
        now = q.popleft()
        
        order = strahler[now][0] + strahler[now][1]
        for nxt in graph[now]:
            in_degree[nxt] -= 1
            if not strahler[nxt] or strahler[nxt][0] < order:
                strahler[nxt] = [order, 0]
            elif strahler[nxt][0] == order:
                strahler[nxt][1] = 1
            if in_degree[nxt] == 0:
                q.append(nxt)
    print(T, sum(strahler[N]))

for _ in range(int(input())):
    solve()