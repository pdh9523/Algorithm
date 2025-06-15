import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def place_ward():
    q = deque([(i,j)])
    check = arr[i][j]
    if ans[i][j] == ".": return
    ans[i][j] = "."
    while q:
        x,y = q.popleft()

        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                if ans[nx][ny] == ".": continue
                if arr[nx][ny] != check: continue
                ans[nx][ny] = "."
                q.append((nx,ny))

dr = [(1,0),(0,1),(-1,0),(0,-1)]
cmd = { "D": 0, "R": 1, "U": 2, "L": 3 }

N,M = map(int,input().split())
arr = [input() for _ in range(N)]

i,j = map(lambda x: int(x)-1, input().split())
commands = input()

ans = [["#"] * M for _ in range(N)]

for command in commands:
    if command == "W": place_ward()
    else:
        i,j = i + dr[cmd[command]][0], j + dr[cmd[command]][1]

for dx,dy in dr + [(0,0)]:
    nx,ny = i+dx, j+dy
    if 0 <= nx < N and 0 <= ny < M:
        ans[nx][ny] = "."

for a in ans:
    print(*a, sep="")