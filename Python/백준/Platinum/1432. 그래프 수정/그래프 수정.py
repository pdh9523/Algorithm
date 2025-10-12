import sys; input = lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush


N = int(input())
arr = [[*map(int, list(input()))] for _ in range(N)]
hq = []
graph = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            graph[j+1].append(i+1)
            in_degree[i+1] += 1
    
    if in_degree[i+1] == 0:
        heappush(hq, -(i+1))

ans = [0] * (N+1)
test = []
num = N
while hq:
    now = -heappop(hq)
    ans[now] = num
    num -= 1
    for nxt in graph[now]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            heappush(hq, -nxt)

print(-1) if not all(ans[1:]) else print(*ans[1:])