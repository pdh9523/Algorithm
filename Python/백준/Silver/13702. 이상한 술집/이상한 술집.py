import sys; input = sys.stdin.readline


def calc_glasses(num):
    res = 0
    for a in arr:
        res += a//num
    return res
N,M = map(int,input().split())
arr = [int(input()) for _ in range(N)]

left = 0
right = 2**31-1
while left <= right:
    mid = (left+right) // 2
    if calc_glasses(mid) >= M:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)