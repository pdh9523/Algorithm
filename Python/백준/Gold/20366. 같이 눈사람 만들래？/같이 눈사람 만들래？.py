N = int(input())
arr = sorted(map(int,input().split()))

ans = float('inf')
for i in range(N-1):
    for j in range(i+1, N):
        now = arr[i] + arr[j]

        left = 0
        right = N-1
        while left < right:
            if left in (i,j):
                left += 1
            elif right in (i,j):
                right -= 1
            elif arr[left] + arr[right] > now:
                ans = min(ans, abs(now-arr[left]-arr[right]))
                right -= 1
            else:
                ans = min(ans, abs(now-arr[left]-arr[right]))
                left += 1
        if ans == 0: break

print(ans)
