import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def dijkstra(home):
    hq = []
    distance = [float('inf')] * (N+1)
    for x in home:
        distance[x] = 0
        heappush(hq, (0,x))

    while hq:
        dist_now, now = heappop(hq)

        if dist_now > distance[now]: continue

        for nxt, cost in graph[now]:
            if distance[nxt] > distance[now] + cost:
                distance[nxt] = distance[now] + cost
                heappush(hq, (distance[nxt], nxt))
    return distance

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
J,K = int(input()), int(input())

arr,brr = [*map(int,input().split())], [*map(int,input().split())]

for _ in range(M):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))

first = dijkstra(arr)
second = dijkstra(brr)

a = first[J]
b = second[J]

if a == b == float('inf'):
    exit(print(-1))

if a <= b:
    print('A')
    print(a)
else:
    print('B')
    print(b)