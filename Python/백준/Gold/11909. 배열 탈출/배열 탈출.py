import sys; input = sys.stdin.readline

N = int(input())
arr = [[*map(int,input().split())] for _ in range(N)]
DP = [[0]*N for _ in range(N)]

for x in range(N):
    for y in range(N):
        if x==0 and y==0: continue

        nx = DP[x-1][y] + (0 if arr[x][y] < arr[x-1][y] else arr[x][y]-arr[x-1][y]+1) if x else float('inf')
        ny = DP[x][y-1] + (0 if arr[x][y] < arr[x][y-1] else arr[x][y]-arr[x][y-1]+1) if y else float('inf')

        DP[x][y] = min(nx,ny)

print(DP[N-1][N-1])
