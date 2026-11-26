import sys; input = sys.stdin.readline


N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

distance = [[float('inf')] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    distance[a][b] = 2
    distance[b][a] = 2

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j])
ans = float('inf')
point = (0,0)
for i in range(N+1):
    for j in range(i+1, N+1):
        tmp = 0
        for k in range(1, N+1):
            if k == i or k == j: continue
            tmp += min(distance[i][k], distance[j][k])
        if ans > tmp:
            ans = tmp
            point = (i,j)
print(*point, ans)