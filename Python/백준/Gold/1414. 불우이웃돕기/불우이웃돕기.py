import sys; input = lambda: sys.stdin.readline().rstrip()
from heapq import heappop, heappush


def parse(char):
    global ans
    res = 0
    
    if char.isupper(): res = ord(char) - ord("A") + 27
    elif char.islower(): res = ord(char) - ord("a") + 1

    ans += res
    return res

ans = 0

N = int(input())
arr = [[parse(char) for char in input()] for _ in range(N)]
graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        graph[i].append((arr[i][j],j))
        graph[j].append((arr[i][j],i))

hq = [(0,0)]
visit = [False] * N
while hq:
    dist_now, now = heappop(hq)
    if visit[now]: continue

    visit[now] = True
    ans -= dist_now

    for cost,nxt in graph[now]:
        if visit[nxt]: continue
        if cost == 0: continue
        heappush(hq, (cost, nxt))

print(ans if all(visit) else -1)