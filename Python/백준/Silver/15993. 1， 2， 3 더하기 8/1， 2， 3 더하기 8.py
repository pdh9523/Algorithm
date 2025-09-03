import sys; input = sys.stdin.readline


MOD = 1000000009
SIZE = 100001
DP = [[0]*SIZE for _ in range(2)]
DP[1][1] = 1
DP[1][2] = 1
DP[1][3] = 1
for i in range(2,SIZE):
    for x in range(2):
        DP[1-x][i] = (DP[1-x][i] + DP[x][i-1] + DP[x][i-2] + DP[x][i-3]) % MOD

for _ in range(int(input())):
    N = int(input())
    print(DP[1][N], DP[0][N])