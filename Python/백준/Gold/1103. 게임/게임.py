import sys; input = lambda: sys.stdin.readline().rstrip(); sys.setrecursionlimit(10000)

def dfs(x=0,y=0):
    if not (0 <= x < N and 0 <= y < M) or arr[x][y] == -1:
        return 0
    
    if visit[x][y]:
        return float('inf')
    
    if DP[x][y] != -1:
        return DP[x][y]

    visit[x][y] = True
    res = 0
    for dx, dy in dr:
        nx, ny = x + dx*arr[x][y], y + dy*arr[x][y]
        res = max(res, dfs(nx, ny))
    visit[x][y] = False

    DP[x][y] = res + 1
    
    return DP[x][y]

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
arr = [[*map(lambda x: -1 if x == "H" else int(x),list(input()))] for _ in range(N)]

DP = [[-1]*M for _ in range(N)]
visit = [[False]*M for _ in range(N)]

ans = dfs()
print(-1 if ans >= float('inf') else ans)
