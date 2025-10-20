MOD = 998244353


N = int(input())
DP = [[0] * 8 for _ in range(N+1)]
DP[0][0] = 1

for i in range(1,N+1):
    for j in range(8):
        if j==0:
            DP[i][j] = DP[i-1][j] * 6 % MOD
        elif j != 7:
            DP[i][j] = (DP[i-1][j-1] + DP[i-1][j] * 6) % MOD
        else:
            DP[i][j] = (DP[i-1][j-1] + DP[i-1][j] * 7) % MOD

print(DP[-1][-1])