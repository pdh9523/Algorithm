import sys; input = sys.stdin.readline


N,M = map(int,input().split())

distance = [[float('inf')] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    distance[a][b] = 0
    distance[b][a] = 1-c

for k in range(N+1):
    distance[k][k] = 0
    for i in range(N+1):
        for j in range(N+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for _ in range(int(input())):
    a,b = map(int,input().split())
    print(distance[a][b])