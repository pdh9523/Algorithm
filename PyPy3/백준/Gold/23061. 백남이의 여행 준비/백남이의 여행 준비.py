import sys; input = sys.stdin.readline


N,M = map(int,input().split())
arr = sorted([[*map(int,input().split())] for _ in range(N)], key=lambda x: -x[1])
bags = [int(input()) for _ in range(M)]
max_size = max(bags)

DP = [0] * (max_size+1)
for w,v in arr:
    for i in range(max_size, w-1, -1):
        DP[i] = max(DP[i], DP[i-w]+v)

for i in range(1,max_size+1):
    if not DP[i] or DP[i-1] > DP[i]:
        DP[i] = DP[i-1]

max_v = -1
ans = -1
for idx, bag in enumerate(bags, start=1):
    val = DP[bag] / bag
    if max_v < val:
        max_v = val
        ans = idx
print(ans)