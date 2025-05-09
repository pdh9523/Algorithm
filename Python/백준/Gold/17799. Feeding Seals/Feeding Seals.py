N,K = map(int,input().split())
arr = sorted(map(int,input().split()))

ans = 0
left, right = 0, N-1
while left <= right:
    if arr[left] + arr[right] <= K:
        left += 1
    right -= 1
    ans += 1

print(ans)