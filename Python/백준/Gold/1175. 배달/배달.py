import sys; input = lambda: sys.stdin.readline().strip()
from collections import deque


def bfs(i,j,d=-1):
    visit = [[0]*M for _ in range(N)]
    dr = [[0]*M for _ in range(N)]

    visit[i][j] = 1
    q = deque([(i,j,d)])

    while q:
        x,y,d = q.popleft()

        if arr[x][y] == "C":
            arr[x][y] = "S"
            return visit[x][y]-1, d

        for i in range(4):
            if d == i: continue

            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if dr[nx][ny] & 1<<i: continue
                if arr[nx][ny] == "#": continue
                dr[nx][ny] += 1<<i
                visit[nx][ny] = visit[x][y]+1
                q.append((nx,ny,i))
    return -1,-1

def find(char):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == char:
                arr[i][j] = "."
                return i,j

dx = 1, 0, -1, 0
dy = 0, 1, 0, -1

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

ans = 0
d = -1
for _ in range(2):
    tmp, d = bfs(*find("S"), d)
    if tmp == -1: 
        ans = -1
        break
    ans += tmp 
print(ans)