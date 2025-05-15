import sys; input = sys.stdin.readline


def dfs(graph, start):
    visit = [0] * (N+1)
    stack = [start]
    while stack:
        now = stack.pop()

        if visit[now]: continue
        visit[now] = 1
        for nxt in graph[now]:
            stack.append(nxt)
    return visit

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
reversed_graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    reversed_graph[b].append(a)

visit = dfs(graph, 1)
reversed_visit = dfs(reversed_graph, N)

for _ in range(int(input())):
    x = int(input())
    print("Defend" if visit[x]+reversed_visit[x] == 2 else "Destroyed", "the CTP")