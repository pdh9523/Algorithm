import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


dr = (1,0),(0,1),(-1,0),(0,-1)

def find(char):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == char:
                if 0 < i < N-1:
                    if arr[i-1][j] == arr[i+1][j] == char:
                        arr[i-1][j] = arr[i][j] = arr[i+1][j] = "0"
                        return i,j,True
                if 0 < j < N-1:
                    if arr[i][j-1] == arr[i][j+1] == char:
                        arr[i][j-1] = arr[i][j] = arr[i][j+1] = "0"
                        return i,j,False

def is_in_range(x,y,is_vertical):
    if 0+is_vertical <= x < N-is_vertical and 0+(1-is_vertical) <= y < N-(1-is_vertical):
        if is_vertical: 
            for nx in (x-1, x, x+1):
                if arr[nx][y] == "1":
                    return False
        else:
            for ny in (y-1, y, y+1):
                if arr[x][ny] == "1":
                    return False
        return True
    return False

def is_turnable(x,y):
    if 1 <= x < N-1 and 1 <= y < N-1:
        return all(arr[i][j]!="1" for i in (x-1,x,x+1) for j in (y-1,y,y+1))
    return False

N = int(input())
arr = [list(input()) for _ in range(N)]

sx,sy,start_vertical = find("B")
ex,ey,end_vertical = find("E")

q = deque([(sx,sy,start_vertical)])

visit = [[[0]*2 for _ in range(N)] for _ in range(N)]

visit[sx][sy][start_vertical] = 1

while q:
    x,y,is_vertical = q.popleft()

    if x==ex and y==ey and is_vertical==end_vertical:
        exit(print(visit[ex][ey][end_vertical]-1))

    for dx,dy in dr:
        nx,ny = x+dx, y+dy
        if is_in_range(nx,ny,is_vertical):
            if visit[nx][ny][is_vertical]: continue
            visit[nx][ny][is_vertical] = visit[x][y][is_vertical] + 1
            q.append((nx,ny,is_vertical))
        
    if is_turnable(x,y):
        if visit[x][y][1-is_vertical]: continue
        visit[x][y][1-is_vertical] = visit[x][y][is_vertical] + 1
        q.append((x,y,1-is_vertical))

print(0)