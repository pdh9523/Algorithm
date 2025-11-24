import sys; input = sys.stdin.readline


N = int(input())
cards = input().split()

M,K = map(int,input().split())
graph = [[] for _ in range(M+1)]
for _ in range(K):
    *q, c = input().split()
    a, b = map(int, q)
    graph[a].append((b,c))
    graph[b].append((a,c))

DP = [[-1] * (M+1) for _ in range(N+1)]
DP[0][1] = 0
for i in range(N):
    color = cards[i]
    for j in range(1, M+1):
        cost = DP[i][j]
        if cost >= 0:
            for t, c in graph[j]:
                if color == c and DP[i + 1][t] < cost + 1:
                    DP[i + 1][t] = cost + 1
                elif color != c and DP[i + 1][t] < cost:
                    DP[i + 1][t] = cost

print(0 if (ans:=max(DP[-1])) == -1 else ans*10)