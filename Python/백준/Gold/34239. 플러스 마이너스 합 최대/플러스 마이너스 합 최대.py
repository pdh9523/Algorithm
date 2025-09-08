import sys; input = sys.stdin.readline


N = int(input())
arr = [*map(int,input().split())]

prefix_sum = [0] * (N+1)
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + (-1)**i * arr[i-1]

ans = arr[0]

max_p_even = 0
min_p_odd = float('inf')

for r in range(1, N+1):
    tmp = max_p_even - prefix_sum[r]
    ans = max(ans, tmp)

    if min_p_odd != float('inf'):
        tmp = prefix_sum[r] - min_p_odd
        ans = max(ans, tmp)

    if r % 2:
        min_p_odd = min(min_p_odd, prefix_sum[r])
    else:
        max_p_even = max(max_p_even, prefix_sum[r])

print(ans)