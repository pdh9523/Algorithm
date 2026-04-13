import sys; input = sys.stdin.readline
from collections import deque

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M,K = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

dist = [[-1]*M for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 3:
            q.append((i,j))
            dist[i][j] = 0
        elif arr[i][j] == 4:
            sx, sy = i, j

while q:
    x, y = q.popleft()
    for dx, dy in dr:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if dist[nx][ny] != -1:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

q = deque([(sx, sy)])
visit = [[-1]*M for _ in range(N)]
visit[sx][sy] = 0

while q:
    x,y = q.popleft()

    if arr[x][y] == 2:
        exit(print(visit[x][y]))

    for dx,dy in dr:
        nx,ny = x+dx, y+dy

        if not (0 <= nx < N and 0 <= ny < M): continue
        if visit[nx][ny] != -1: continue
        if arr[nx][ny] == 1: continue
        if dist[nx][ny] != -1 and dist[nx][ny] <= K: continue

        visit[nx][ny] = visit[x][y] + 1
        q.append((nx, ny))

print(-1)