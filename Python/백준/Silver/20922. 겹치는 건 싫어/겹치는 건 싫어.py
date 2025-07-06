N,K = map(int,input().split())
arr = [*map(int,input().split())]

cnt = [0]*100001

left,right=0,0

ans = 0
while right < N:
    if cnt[arr[right]] < K:
        cnt[arr[right]] += 1
        right += 1
    else:
        cnt[arr[left]] -= 1
        left += 1

    ans = max(ans, right-left)
print(ans)