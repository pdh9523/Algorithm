def check(now):
    pos,cnt = 0,0
    for i in range(N+2):
        if arr[i] - pos > now:
            cnt += 1
            now = mid
        now -= (arr[i] - pos)
        pos = arr[i]
    return cnt <= K

L,N,K = map(int,input().split())
arr = [0] + [*map(int,input().split())] + [L]

max_dist = max(arr[i+1]-arr[i] for i in range(N+1))

left,right = max_dist, L
ans = 0
while left <= right:
    mid = (left+right)//2
    
    if check(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)