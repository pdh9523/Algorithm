SIZE = 31
DP = [[0]*SIZE for _ in range(SIZE)]
for i in range(SIZE):
    DP[0][i] = 1
for i in range(1,SIZE):
    for j in range(i,SIZE):
        DP[i][j] = DP[i-1][j] + DP[i][j-1]
while (N:=int(input())): print(DP[N][N])
