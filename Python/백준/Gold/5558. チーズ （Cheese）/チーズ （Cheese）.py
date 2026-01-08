import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


dr = (1,0),(0,1),(-1,0),(0,-1)

def findAll():
    data = dict()

    for i in range(N):
        for j in range(M):
            if arr[i][j].isnumeric():
                data[int(arr[i][j])] = (i,j)
            elif arr[i][j] == "S":
                data[0] = (i,j)
    return data

def bfs(now=0):
    if now == K: return 0

    sx,sy = position[now]
    ex,ey = position[now+1]

    q = deque([(sx,sy)])

    visit = [[-1]*M for _ in range(N)]
    visit[sx][sy] = 0

    while q:
        x,y = q.popleft()

        if (x,y) == (ex,ey): break

        for dx,dy in dr:
            nx,ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == "X": continue
                if visit[nx][ny] != -1: continue

                visit[nx][ny] = visit[x][y] + 1
                q.append((nx,ny))
    
    res = visit[ex][ey]
    del visit
    return res + bfs(now+1)


N,M,K = map(int,input().split())
arr = [input() for _ in range(N)]
position = findAll()

print(bfs())