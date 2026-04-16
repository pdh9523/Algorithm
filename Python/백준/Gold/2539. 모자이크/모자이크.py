import sys; input = sys.stdin.readline

def bs(p):
    now = arr[0]
    res = 1
    for x in arr:
        if x >= now + p:
            res += 1
            now = x
    return res

N,M = map(int,input().split())
K = int(input())
arr = sorted([[*map(int,input().split())] for _ in range(int(input()))],key=lambda x:x[1])
left,right,ans = max(x for x,y in arr), 10**7, 0
arr = [x[1] for x in arr]
while left <= right:
    mid = (left+right) // 2
    if bs(mid) <= K:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
