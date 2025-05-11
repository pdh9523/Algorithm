def check(num):
    DP = [1] * N

    for i in range(N):
        tmp = arr[i] - T + 1
        if i < num:
            DP[i] = max(tmp, DP[i])
        else:
            DP[i] = max(DP[i-num] + T, tmp, DP[i])
    
    for i in range(N):
        if DP[i] > arr[i]: return False
    return True

N,T = map(int,input().split())
arr = sorted(map(int,input().split()))

left,right = 0, N+1

while left + 1 < right:
    mid = (left+right) // 2

    if check(mid):
        right = mid
    else:
        left = mid

print(right)