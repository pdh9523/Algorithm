import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def find(char):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == char:
                return i,j

N,M = map(int,input().split())
arr = [input() for _ in range(N)]
x,y = find("B")

q = deque([(x,y)])
visit = [[0]*M for _ in range(N)]
visit[x][y] = 1
while q:
    x,y = q.popleft()

    if arr[x][y] == "C":
        exit(print(visit[x][y]-1))
    
    for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
        nx,ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == "*": continue
            if visit[nx][ny]: continue
            visit[nx][ny] = visit[x][y] + 1
            q.append((nx,ny))
