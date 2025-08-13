import sys; input = lambda: sys.stdin.readline().rstrip()


def backtrack(coins, idx=0):
    global ans
    if len(coins) == 1:
        ans = min(ans, idx)
        return
    
    if len(coins) == 0: return
    if idx >= 10: return
    if ans < idx: return
    
    for dx,dy in dr:
        nxt_coins=[]
        for x,y in coins:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == "#":
                    nxt_coins.append((x,y))
                else:
                    nxt_coins.append((nx,ny))
        backtrack(nxt_coins, idx+1)

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

coins = []
for i in range(N):
    for j in range(M):
        if arr[i][j] =="o":
            arr[i][j] = "."
            coins.append((i,j))
ans = float('inf')
backtrack(coins)
print(-1 if ans == float('inf') else ans)