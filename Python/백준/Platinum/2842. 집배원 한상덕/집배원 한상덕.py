import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def find(char):
    res = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == char:
                res.append((i,j))
    return res

def bfs(lower, upper):
    if not (lower <= weight[sx][sy] <= upper):
        return False
    visit = [[False]*N for _ in range(N)]
    visit[sx][sy] = True
    q = deque([(sx,sy)])

    cnt = 0
    while q:
        x,y = q.popleft()
        
        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if not (lower <= weight[nx][ny] <= upper): continue
                if visit[nx][ny]: continue

                if arr[nx][ny] == "K": cnt += 1
                visit[nx][ny] = True

                q.append((nx,ny))
    return k_cnt == cnt


dr = (1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)

N = int(input())
arr = [input() for _ in range(N)]
weight = [[*map(int,input().split())] for _ in range(N)]
sx,sy = find("P").pop()

k_cnt = len(set(find("K")))

sorted_weight = sorted(set(weight[i][j] for i in range(N) for j in range(N)))
left,right = 0, 0

ans = float('inf')
while left <= right < len(sorted_weight):
    if bfs(sorted_weight[left],sorted_weight[right]):
        ans = min(ans, sorted_weight[right]-sorted_weight[left])
        left += 1
    else: right += 1
print(ans)