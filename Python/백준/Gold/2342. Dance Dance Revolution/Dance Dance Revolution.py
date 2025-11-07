import sys; sys.setrecursionlimit(10**5)


def move(a, b):
    if a==0: return 2
    elif a==b: return 1
    elif abs(a-b)==2: return 4
    else: return 3

arr = [*map(int,input().split())]
length = len(arr)
DP = [[[float('inf')] * 5 for _ in range(5)] for _ in range(length)]
DP[0][0][0] = 0

for i in range(length-1):
    nxt = arr[i]
    for left in range(5):
        for right in range(5):
            DP[i+1][left][nxt] = min(DP[i+1][left][nxt], DP[i][left][right] + move(right, nxt))
            DP[i+1][nxt][right] = min(DP[i+1][nxt][right], DP[i][left][right] + move(left, nxt))

print(min(map(min, DP[length-1])))