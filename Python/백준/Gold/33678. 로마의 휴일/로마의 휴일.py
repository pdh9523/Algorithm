import sys; input = sys.stdin.readline
from bisect import bisect_left, bisect_right


N,K,X = map(int,input().split())
arr = [*map(int,input().split())]

left_sum = [0] * (N+1)
left_sum[1] = arr[0] * X
for i in range(2,N+1):
    left_sum[i] = left_sum[i-1] + (arr[i-1] * X)

right_sum = [0] * (N+1)
right_sum[1] = arr[-1]
for i in range(2,N+1):
    right_sum[i] = right_sum[i-1] + arr[N-i]

ans = 0
for i in range(N):
    left = left_sum[i]
    b = bisect_left(right_sum, K-left)
    
    if i + b >= N: continue

    if left + right_sum[b] >= K:
        ans = max(ans, N-i-b)

print(ans if ans > 0 else -1)
