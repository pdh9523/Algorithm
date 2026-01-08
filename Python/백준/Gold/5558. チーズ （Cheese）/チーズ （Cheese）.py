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

    q = deque([(sx,sy,0)])
    visit[sx][sy] = now
    while q:
        x,y,cnt = q.popleft()

        if (x,y) == (ex,ey):
            return cnt + bfs(now+1)

        for dx,dy in dr:
            nx,ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < M:
                if visit[nx][ny] >= now: continue
                visit[nx][ny] = now
                q.append((nx,ny,cnt+1))

N,M,K = map(int,input().split())
arr = [input() for _ in range(N)]
position = findAll()

visit = [[K if arr[i][j] == "X" else -1 for j in range(M)] for i in range(N)]
print(bfs())