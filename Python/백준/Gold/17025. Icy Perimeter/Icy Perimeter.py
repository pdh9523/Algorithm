import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque

dr = (1,0),(0,1),(-1,0),(0,-1)

def bfs(x,y):
    q = deque([(x,y)])
    visit[x][y] = True
    v_cnt = 1
    l_cnt = 0
    while q:
        x,y = q.popleft()

        for dx,dy in dr:
            nx,ny = x+dx,y+dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == "#":
                if visit[nx][ny]: continue
                visit[nx][ny] = True
                v_cnt += 1
                q.append((nx,ny))
            else: l_cnt += 1

    return v_cnt, l_cnt

N = int(input())
arr = [input() for _ in range(N)]

visit = [[False]*N for _ in range(N)]

max_volume = 0
max_length = 0
for i in range(N):
    for j in range(N):
        if visit[i][j]: continue
        if arr[i][j] == ".": continue
        volume, length = bfs(i,j)
        if volume > max_volume:
            max_volume = volume
            max_length = length
        elif max_volume == volume:
            max_length = min(max_length, length)
print(max_volume, max_length)