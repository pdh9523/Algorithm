import sys; input = sys.stdin.readline
from collections import deque


def bfs(q):
    global ans

    next_q = deque()
    while q:
        x,y = q.popleft()

        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if arr[nx][ny] == 0:
                arr[nx][ny] = 1
                ans += 1
                next_q.append((nx,ny))
    return next_q

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
SIZE = 3050
arr = [[0]*SIZE for _ in range(SIZE)]
ans = 0
q = deque()
for i in range(N):
    tmp = input()
    for j in range(M):
        if tmp[j] == "o": 
            ans += 1
            arr[i][j] = 1
            q.append((i,j))

for _ in range(int(input())):
    q = bfs(q)

print(ans)