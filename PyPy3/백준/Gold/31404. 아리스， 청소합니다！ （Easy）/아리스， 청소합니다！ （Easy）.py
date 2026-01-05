import sys; input = lambda: sys.stdin.readline().rstrip()


dr = (-1,0),(0,1),(1,0),(0,-1)

N,M = map(int,input().split())
x,y,d = map(int,input().split())

arr = [[*map(int,list(input()))] for _ in range(N)]
brr = [[*map(int,list(input()))] for _ in range(N)]

a_visit = [[False]*M for _ in range(N)]
b_visit = [[0]*M for _ in range(N)]
ans = 0
now = 0
while True:
    now += 1
    if a_visit[x][y]:
        if b_visit[x][y] & 1<<(d%4): break
        b_visit[x][y] |= 1<<(d%4)
        d += brr[x][y]
    else:
        a_visit[x][y] = True
        b_visit = [[0]*M for _ in range(N)]
        ans = now
        d += arr[x][y]

    dx,dy = dr[d%4]
    x,y = x+dx,y+dy
    if not (0 <= x < N and 0 <= y < M): break

print(ans)