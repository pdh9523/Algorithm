import sys; input = sys.stdin.readline


N,M = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(M)]
length = N+101
DP = [float('inf')] * length
DP[0] = 0

for c,v in arr:
    for i in range(v, length):
        DP[i] = min(DP[i], DP[i-v]+c)

print(min(DP[N:]))