import sys; input = sys.stdin.readline


def binary_search(diff):
    res = 0
    for i in range(1,N+2):
        x = arr[i] - arr[i-1]
        res += (x-1) // diff
    return res <= M
    

N,M,L = map(int,input().split())
arr = [0] + (sorted(map(int,input().split())) if N else []) + [L]

left, right = 1, L
while left < right:
    mid = (left+right) // 2
    if binary_search(mid):
        right = mid
    else:
        left = mid+1
print(right)