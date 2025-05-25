import sys; input = sys.stdin.readline


N = int(input())
arr = [*zip(map(int,input().split()), map(int,input().split()))]

DP = [-1] * 100
DP[0] = 0

for i,j in arr:
    for k in range(99, -1, -1):
        if DP[k] == -1: continue
        if k+i >= 100: continue
        DP[k+i] = max(DP[k+i], DP[k]+j)

print(max(DP))