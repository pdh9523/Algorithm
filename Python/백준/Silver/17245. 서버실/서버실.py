import sys; input = sys.stdin.readline


def check(num):
    res = 0
    for i in range(N):
        for j in range(N):
            res += min(arr[i][j], num)    
    return res >= total / 2

N = int(input())
arr = [[*map(int,input().split())] for _ in range(N)]
total = sum(sum(a) for a in arr)
left, right = 0, 10000000
while left < right:
    mid = (left+right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1
print(right)