N = int(input())
arr = iter(map(int,input().split()))

DP = [0] * N

min_v = next(arr)
for i,x in enumerate(arr, start=1):
    DP[i] = max(DP[i-1], x-min_v)
    min_v = min(min_v, x)
print(*DP)