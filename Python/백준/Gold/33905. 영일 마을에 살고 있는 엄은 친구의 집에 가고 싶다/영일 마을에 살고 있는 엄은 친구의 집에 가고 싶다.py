import sys; input = sys.stdin.readline


N,M,K = map(int,input().split())

graph = [[] for _ in range(N+2)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

excludes = set(map(int,input().split()))

visit = [False] * (N+2)
stack = [1]
while stack:
    now = stack.pop()

    if visit[now]: continue
    visit[now] = True

    for nxt in graph[now]:
        if nxt in excludes: continue
        stack.append(nxt)

ans = 0
for i in range(2,N+2):
    ans += visit[i]
print(ans)