import sys; input = lambda: sys.stdin.readline().rstrip()


MOD = 10**9+9

N,M = map(int,input().split())
arr = [input() for _ in range(N)]

DP = [[1]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == "X": continue
        if arr[i][j] != "E":
            DP[i+1][j] = (DP[i+1][j] + DP[i][j]) % MOD
        if arr[i][j] != "S":
            DP[i][j+1] = (DP[i][j+1] + DP[i][j]) % MOD
            
print(DP[i][j])