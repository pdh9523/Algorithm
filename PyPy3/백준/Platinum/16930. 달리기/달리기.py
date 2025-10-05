import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


dr = (1,0),(0,1),(-1,0),(0,-1)

N,M,K = map(int,input().split())
arr = [input() for _ in range(N)]
sx,sy,ex,ey = map(lambda x: int(x)-1,input().split())

q = deque([(sx,sy)])
visit = [[float('inf')]*M for _ in range(N)]
visit[sx][sy] = 0

while q:
    x,y = q.popleft()

    for dx,dy in dr:
        for w in range(1,K+1):
            nx,ny = x+dx*w, y+dy*w

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] =="#": break
                if visit[nx][ny] <= visit[x][y]: break
                if visit[nx][ny] != float('inf'): continue
                visit[nx][ny] = visit[x][y] + 1

                q.append((nx,ny))

print(visit[ex][ey] if visit[ex][ey] != float('inf') else -1)
