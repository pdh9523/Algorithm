import sys; input = sys.stdin.readline
from heapq import heappop, heappush
from collections import defaultdict

INF = float('inf')

M, N, K = map(int, input().split())

sero = defaultdict(list)
garo = defaultdict(list)

sero[1].append((0, 0))

for i in range(1, K + 1):
    m, n = map(int, input().split())
    sero[m].append((n, i))
    garo[n].append((m, i))

sero[M].append((N, K + 1))
garo[N].append((M, K + 1))

graph = defaultdict(list)

for i in range(1, K + 1):
    graph[i * 2].append((i * 2 + 1, 1))
    graph[i * 2 + 1].append((i * 2, 1))

for lst in garo.values():
    lst.sort()
for lst in sero.values():
    lst.sort()

for i in range(N + 1):
    for j in range(len(garo[i]) - 1):
        dist = garo[i][j + 1][0] - garo[i][j][0]
        u = garo[i][j + 1][1]
        v = garo[i][j][1]
        graph[u * 2].append((v * 2, dist))
        graph[v * 2].append((u * 2, dist))

for i in range(M + 1):
    for j in range(len(sero[i]) - 1):
        dist = sero[i][j + 1][0] - sero[i][j][0]
        u = sero[i][j + 1][1]
        v = sero[i][j][1]
        graph[u * 2 + 1].append((v * 2 + 1, dist))
        graph[v * 2 + 1].append((u * 2 + 1, dist))

dist_arr = [INF] * ((K + 2) * 2)
pq = [(-1, 1)]
dist_arr[1] = -1

while pq:
    cur_dist, cur_id = heappop(pq)

    if dist_arr[cur_id] < cur_dist:
        continue

    for next_id, next_dist in graph[cur_id]:
        new_dist = cur_dist + next_dist

        if dist_arr[next_id] > new_dist:
            dist_arr[next_id] = new_dist
            heappush(pq, (new_dist, next_id))

result = min(dist_arr[(K + 1) * 2], dist_arr[(K + 1) * 2 + 1])
print(-1 if result == INF else result)
