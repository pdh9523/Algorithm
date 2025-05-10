import sys; input = lambda: sys.stdin.readline().strip()
from collections import deque


def bfs():
    visit = [[0]*N for _ in range(N)]
    visit[sx][sy] = H

    q = deque([(sx,sy,H,0,0)])
    while q:
        x,y,now_h,now_d,cnt = q.popleft()

        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 'E': return cnt+1
                nxt_h, nxt_d = now_h, now_d
                if arr[nx][ny] == 'U':
                    nxt_d = D

                if nxt_d == 0:
                    nxt_h -= 1
                else:
                    nxt_d -= 1

                if nxt_h == 0: continue

                if visit[nx][ny] < nxt_h:
                    visit[nx][ny] = nxt_h
                    q.append((nx,ny,nxt_h,nxt_d,cnt+1))
    return -1

def find(char):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == char:
                return i,j

dr = (1,0),(0,1),(-1,0),(0,-1)

N,H,D = map(int,input().split())
arr = [input() for _ in range(N)]
sx,sy = find("S")

print(bfs())