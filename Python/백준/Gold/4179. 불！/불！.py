'''
불!

BFS
'''
import sys; input = lambda: sys.stdin.readline().strip()
from collections import deque


def find(char):
    res = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == char:
                visit[i][j] = 1
                res.append((i,j))
    return deque(res)

def bfs_fire():
    next_fires = deque()
    while fires:
        x,y = fires.popleft()

        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == "#": continue
                if arr[nx][ny] == "F": continue
                arr[nx][ny] = "F"
                next_fires.append((nx,ny))
    return next_fires

def bfs_man():
    global ans
    next_mans = deque()

    while mans:
        x,y = mans.popleft()
        if x == 0 or x == N-1 or y == 0 or y == M-1:
            ans = visit[x][y]
            return
        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] != ".": continue
                if visit[nx][ny]: continue
                visit[nx][ny] = visit[x][y] + 1
                next_mans.append((nx,ny))
    return next_mans


dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
visit = [[0]*M for _ in range(N+1)]
mans = find("J")
fires = find("F")
ans = 0
while not ans and len(mans):
    fires = bfs_fire()
    mans = bfs_man()

print(ans if ans else "IMPOSSIBLE")