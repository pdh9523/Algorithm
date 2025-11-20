import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def find(char):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == char:
                return i,j

def bfs(x,y):
    visit = [[-1]*M for _ in range(N)]
    q = deque([(x,y)])
    visit[x][y] = 0
    while q:
        x,y = q.popleft()

        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                if visit[nx][ny] != -1: continue
                if arr[nx][ny] == "I": continue
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx,ny))
    return visit

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())

arr = [input() for _ in range(N)]

data = bfs(*find("V"))
pirates = [[float('inf')]*M for _ in range(N)]
for x in range(N):
    for y in range(M):
        if data[x][y] == -1: continue
        min_v = data[x][y] 
        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            while 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != "I":
                min_v = min(min_v, data[nx][ny])
                nx += dx
                ny += dy
        pirates[x][y] = min_v

sx,sy = find("Y")

q = deque([(sx,sy)])
visit = [[-1]*M for _ in range(N)]
visit[sx][sy] = 0

while q:
    x,y = q.popleft()

    if arr[x][y] == "T":
        exit(print("YES"))

    for dx,dy in dr:
        nx,ny = x+dx,y+dy
        if 0 <= nx < N and 0 <= ny < M:
            if visit[nx][ny] != -1: continue
            if arr[nx][ny] == "I": continue
            if visit[x][y] + 1 >= pirates[nx][ny]: continue

            visit[nx][ny] = visit[x][y] + 1
            q.append((nx,ny))
print("NO")