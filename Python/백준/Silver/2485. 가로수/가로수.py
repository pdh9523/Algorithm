import sys; input = sys.stdin.readline
from math import gcd

N = int(input())
tmp = [int(input()) for _ in range(N)]

arr = [tmp[i+1] - tmp[i] for i in range(N-1)]

x = arr[0]
for i in range(1, len(arr)):
    x = gcd(x, arr[i])

print(sum(a//x-1 for a in arr))
