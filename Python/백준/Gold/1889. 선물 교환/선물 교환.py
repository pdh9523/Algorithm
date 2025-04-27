import sys; input = sys.stdin.readline
from collections import deque


N = int(input())
graph = [[] for _ in range(N+1)]
degrees = [0] * (N+1)

for i in range(1,N+1):
    for j in map(int,input().split()):
        graph[i].append(j)
        degrees[j] += 1

q = deque([i for i in range(1, N+1) if degrees[i] < 2])
visit = [False] * (N+1)

while q:
    now = q.popleft()
    if visit[now]: continue
    visit[now] = True

    for nxt in graph[now]:
        degrees[nxt] -= 1
        if degrees[nxt] < 2:
            q.append(nxt)

ans = [i for i in range(1,N+1) if degrees[i] == 2]
print(len(ans))
if ans: print(*ans)
