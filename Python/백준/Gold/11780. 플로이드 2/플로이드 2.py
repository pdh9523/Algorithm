import sys; input = sys.stdin.readline


N = int(input())
distance = [[float('inf')]*(N+1) for _ in range(N+1)]
ans = [[[] for _ in range(N+1)] for _ in range(N+1)]
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    distance[a][b] = min(distance[a][b], c)
    ans[a][b] = [b]

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                ans[i][j] = ans[i][k] + ans[k][j]
    distance[k][k] = 0
    ans[k][k] = []

for i in range(1, N+1):
    for j in range(1, N+1):
        print(0 if distance[i][j] == float('inf') else distance[i][j], end=" ")
    print()

for i in range(1, N+1):
    for j in range(1, N+1):
        if not len(ans[i][j]):
            print(0)
        else:
            print(len(ans[i][j])+1, *[i] + ans[i][j])
