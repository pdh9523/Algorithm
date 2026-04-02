import sys; input = sys.stdin.readline

def get_count(arr):
    return sum(1 for x in arr if x != float('inf'))

N,M = map(int,input().split())

distance = [[float('inf')]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    distance[a][b] = 1

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            distance[i][j] = min(distance[i][j],(distance[i][k]+distance[k][j]))

ans = 0
for i in range(1,N+1):
    if get_count(distance[i]) > N//2 or get_count([distance[j][i] for j in range(N+1)]) > N//2:
        ans += 1
print(ans)