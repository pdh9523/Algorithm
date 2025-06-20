import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


dr = (1,0),(0,1),(-1,0),(0,-1)

def solve():
    M,N = map(int,input().split())
    arr = [list(input()) for _ in range(N)]

    fire_visit = [[-1]*M for _ in range(N)]
    person_visit = [[-1]*M for _ in range(N)]

    fire_q = deque()
    person_q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == "*":
                fire_q.append((i,j))
                fire_visit[i][j] = 0
            elif arr[i][j] == "@":
                person_q.append((i,j))
                person_visit[i][j] = 0 
    
    while fire_q:
        x,y = fire_q.popleft()
        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0<= ny < M:
                if arr[nx][ny] == "#": continue
                if fire_visit[nx][ny] != -1: continue
                fire_visit[nx][ny] = fire_visit[x][y] + 1
                fire_q.append((nx,ny))

    while person_q:
        x,y = person_q.popleft()
        for dx,dy in dr:
            nx,ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == "#": continue
                if person_visit[nx][ny] != -1: continue
                if fire_visit[nx][ny] != -1 and fire_visit[nx][ny] <= person_visit[x][y] + 1:
                    continue
                person_visit[nx][ny] = person_visit[x][y] + 1
                person_q.append((nx,ny))
            else:
                return person_visit[x][y] + 1

    return "IMPOSSIBLE"

for _ in range(int(input())):
    print(solve())