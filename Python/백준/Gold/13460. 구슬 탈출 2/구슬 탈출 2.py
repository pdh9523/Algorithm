import sys; input = lambda: sys.stdin.readline().rstrip()


def find(char):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == char: return i,j

def move(r,b,x):
    def roll(x,y, ex=None):
        while True:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != "#" and (nx,ny) != ex:
                if arr[nx][ny] == "O":
                    return -1,-1
                x,y = nx,ny
            else:
                return x,y
    
    dr = (1,0),(0,1),(-1,0),(0,-1)
    dx,dy = dr[x]

    rx,ry = r
    bx,by = b
    routes = set()
    nrx,nry = rx,ry
    while 0 <= nrx < N and 0 <= nry < M and arr[nrx][nry] != "#":
        routes.add((nrx,nry))
        nrx,nry = nrx+dx,nry+dy
    if (bx,by) in routes:
        bx,by = roll(bx,by)
        rx,ry = roll(rx,ry, (bx,by))
    else:
        rx,ry = roll(rx,ry)
        bx,by = roll(bx,by, (rx,ry))
    
    return (rx,ry), (bx,by)

def backtrack(r, b, idx=0):
    global ans
    if idx > 10: return
    if idx > ans: return
    if r == (-1,-1) and b != (-1,-1):
        ans = min(ans, idx)
    for x in range(4):
        nr, nb = move(r,b,x)
        if data.get((nr,nb), float('inf')) <= idx: continue
        data[nr,nb] = data[r,b] + 1
        backtrack(nr,nb,idx+1)

t = []    
N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

r,b = find("R"), find("B")
data = dict()
data[r,b] = 0

ans = float('inf')
backtrack(find("R"), find("B"))
print(ans if ans != float('inf') else -1)
