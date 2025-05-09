import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)


def dfs(now=1):
    global check
    if len(graph[now]):
        for nxt in graph[now]:
            if nxt not in fans:
                dfs(nxt)
    else:
        check = False

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

S = int(input())
fans = set(map(int,input().split()))

check = True
1 in fans or dfs()
print("Yes" if check else "yes")