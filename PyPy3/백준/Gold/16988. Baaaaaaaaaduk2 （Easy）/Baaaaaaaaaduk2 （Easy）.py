import sys; input = sys.stdin.readline
from collections import deque
from copy import deepcopy

def is_nearby(x,y):
    for dx,dy in dr:
        nx,ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 2:
                return True
    return False

def get_index(idx):
    return idx//M, idx%M

def get_comb(idx=0, res=[]):
    if res:
        comb.add(tuple(res))
    
    if len(res) == 2:
        return

    if idx >= N*M: return
    x,y = get_index(idx)
    if arr[x][y] == 0 and is_nearby(x,y):
        get_comb(idx+1, res + [(x,y)])
    get_comb(idx+1, res)

def bfs(arr, sx, sy):
    q = deque([(sx,sy)])
    visit = [[False]*M for _ in range(N)]
    while q:
        x,y = q.popleft()

        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                if visit[nx][ny]: continue
                if arr[nx][ny] == 1: continue
                arr[nx][ny] = -1
                visit[nx][ny] = True
                q.append((nx,ny))

def get_count(arr):
    res = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                res += 1
    return res

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

comb = set()
get_comb()

ans = 0
for c in comb:
    tmp = deepcopy(arr)
    for x,y in c:
        tmp[x][y] = 1
    
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                bfs(tmp, i, j)
    ans = max(ans, get_count(tmp))
print(ans)
