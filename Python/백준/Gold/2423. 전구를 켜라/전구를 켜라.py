import sys; input = lambda: sys.stdin.readline().strip()
from collections import deque


def bfs():
    if (N+M)%2: return -1

    q = deque([(0,0,0)])
    visit = [[False] * (M+1) for _ in range(N+1)]
    while q:
        x,y, dist = q.popleft()
        if visit[x][y]: continue

        visit[x][y] = True
        if x == N and y == M:
            return dist

        for idx, (dx,dy) in enumerate(((1,1),(-1,1),(-1,-1),(1,-1))):
            nx,ny = x+dx, y+dy
            if 0 <= nx <= N and 0 <= ny <= M and not visit[nx][ny]:
                if (idx + arr[x - (dx < 0)][y - (dy < 0)])%2:
                    q.append((nx,ny, dist+1))
                else:
                    q.appendleft((nx,ny, dist))
    return visit[N][M]

N,M = map(int,input().split())
arr = [[*map(lambda x: 1 if x == "/" else 0, input())] for _ in range(N)]
print("NO SOLUTION" if (ans:=bfs()) == -1 else ans)