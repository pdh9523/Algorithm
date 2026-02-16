import sys; input = lambda: sys.stdin.readline().rstrip()

def check(x, y, tile, dr):
    dx,dy = dr
    while 0 <= x < N and 0 <= y < M and arr[x][y] == tile:
        arr[x][y] = ""
        x,y = x+dx, y+dy

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

d = {
    "-": (0,1),
    "|": (1,0),
}
ans = 0
for x in range(N):
    for y in range(M):
        if arr[x][y]:
            check(x,y, arr[x][y], d[arr[x][y]])
            ans += 1
print(ans)