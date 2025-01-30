import sys; input = lambda: sys.stdin.readline().strip()


def find(char):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == char:
                return i,j

def backtrack(x, y, idx=0, result=set()):
    global ans
    if idx == K:
        ans = max(ans, len(result))
        return

    for dx,dy in dr:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == "#": continue
            backtrack(nx, ny, idx+1, result | {(nx,ny)} if arr[nx][ny] == "S" else result)

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M,K = map(int,input().split())
arr = [input() for _ in range(N)]

ans = 0
backtrack(*find("G"))
print(ans)