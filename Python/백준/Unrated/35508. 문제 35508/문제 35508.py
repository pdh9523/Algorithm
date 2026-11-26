import sys; input = sys.stdin.readline
from bisect import bisect_right

N,D = map(int,input().split())
arr = sorted([[*map(int,input().split())] for _ in range(N)])

ans = 0

for T,A,B in arr:
    if T <= D:
        ans = max(ans, A + B)

prefix_a = [0] * N
prefix_b = [0] * N

for i in range(N):
    prefix_a[i] = max(prefix_a[i-1], arr[i][1])
    prefix_b[i] = max(prefix_b[i-1], arr[i][2])

times = [d[0] for d in arr]

for j in range(1, N):
    Tj, Aj, Bj = arr[j]
    target = D - Tj
    if target < 0: continue

    boundary = bisect_right(times, target, 0, j) - 1

    if boundary >= 0:
        ans = max(ans, prefix_a[boundary] + Bj)
        ans = max(ans, Aj + prefix_b[boundary])

print(ans)
