import sys; input = sys.stdin.readline

N,M,T = map(int,input().split())

distance = [[float('inf')] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    distance[a][b] = c

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
                distance[i][j] = min(max(distance[i][k],distance[k][j]), distance[i][j])

for _ in range(T):
    x,y = map(int,input().split())
    print(distance[x][y] if distance[x][y] < float('inf') else -1)
