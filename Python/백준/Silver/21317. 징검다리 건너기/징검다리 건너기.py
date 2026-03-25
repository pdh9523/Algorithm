import sys; input = sys.stdin.readline

N = int(input())
arr = [[*map(int,input().split())] for _ in range(N-1)]
K = int(input())

if N == 1: exit(print(0))
if N == 2: exit(print(arr[0][0]))

DP = [[float('inf')]*2 for _ in range(N)]
DP[0][0] = 0 

for i in range(N):
    DP[i][0] = min(DP[i][0], DP[i-1][0] + arr[i-1][0], DP[i-2][0] + arr[i-2][1])
    DP[i][1] = min(DP[i][1], DP[i-1][1] + arr[i-1][0], DP[i-2][1] + arr[i-2][1], DP[i-3][0] + K)

print(min(DP[-1]))
