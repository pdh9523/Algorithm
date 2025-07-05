import sys; input = sys.stdin.readline


N,M,K = map(int,input().split())

graph = [[] for _ in range(N+2)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (N+2)
for ex in map(int,input().split()): visit[ex] = True

ans = -1
stack = [1]
while stack:
    now = stack.pop()

    if visit[now]: continue
    visit[now] = True
    ans += 1

    for nxt in graph[now]:
        stack.append(nxt)

print(ans)