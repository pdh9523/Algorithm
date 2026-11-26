SIZE = 1000000

DP = [0] * (SIZE+1)
for i in range(1,SIZE+1):
    for j in range(i , SIZE+1, i):
        DP[j] += i

prefix_sum = [0] * (SIZE+1)
for i in range(1, SIZE+1):
    prefix_sum[i] = prefix_sum[i-1] + DP[i]

N = int(input())
ans = [0] * N
for i in range(N):
    ans[i] = prefix_sum[int(input())]

print(*ans, sep="\n")
