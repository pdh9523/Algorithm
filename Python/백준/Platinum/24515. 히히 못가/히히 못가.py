import sys; input = lambda: sys.stdin.readline().strip()
from heapq import heappop, heappush, heapify

def bfs(start, char):
    stack = [start]
    cnt = 0
    while stack:
        x,y = stack.pop()

        if arr[x][y]: continue
        arr[x][y] = idx
        cnt += 1

        for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
            nx,ny = x+dx,y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if tmp[nx][ny] != char: continue
                stack.append((nx,ny))
    data[idx] = cnt

N = int(input())
tmp = [input() for _ in range(N)]

arr = [[0]*N for _ in range(N)]
data = dict()
idx = 1
for i in range(N):
    for j in range(N):
        if arr[i][j]: continue
        if tmp[i][j] == ".": continue
        bfs((i,j), tmp[i][j])
        idx += 1

graph = [set() for _ in range(idx+1)]
for x in range(N):
    for y in range(N):
        for dx,dy in (1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1):
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[x][y] == 0: continue
                if arr[nx][ny] == 0: continue
                if arr[nx][ny] != arr[x][y]:
                    graph[arr[nx][ny]].add(arr[x][y])
                    graph[arr[x][y]].add(arr[nx][ny])

start_node = set()
end_node = set()
for i in range(N):
    if arr[i][0] != 0:
        start_node.add(arr[i][0])
    if arr[N-1][i] != 0:
        start_node.add(arr[N-1][i])
    end_node.add(arr[0][i])
    end_node.add(arr[i][N-1])

distance = [float('inf')] * (idx+1)
hq = [(data[n], n) for n in start_node]
for d,x in hq: distance[x] = d
heapify(hq)

while hq:
    dist_now, now = heappop(hq)

    if dist_now > distance[now]: continue

    for nxt in graph[now]:
        if distance[nxt] > dist_now + data[nxt]:
            distance[nxt] = dist_now + data[nxt]
            heappush(hq, (distance[nxt], nxt))

print(min(distance[end] for end in end_node))