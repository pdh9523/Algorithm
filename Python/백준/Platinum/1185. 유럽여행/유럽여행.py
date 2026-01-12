import sys; input = sys.stdin.readline
from heapq import heappop,heappush


N,M = map(int,input().split())
arr = [0] * (N+1)
start = -1
tmp = float('inf')
for i in range(1,N+1):
    c = int(input())
    if c < tmp:
        start = i
        tmp = c
    arr[i] = c

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((2*c+arr[a]+arr[b], b))
    graph[b].append((2*c+arr[a]+arr[b], a))

visit = [False] * (N+1)
hq = [(0,start)]
ans = arr[start]
while hq:
    cost, now = heappop(hq)

    if visit[now]: continue

    visit[now] = True
    ans += cost

    for nxt in graph[now]:
        heappush(hq, nxt)

print(ans)