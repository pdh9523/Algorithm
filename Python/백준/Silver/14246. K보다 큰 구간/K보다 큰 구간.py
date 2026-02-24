N = int(input())
arr = [*map(int,input().split())]
K = int(input())

left, right = 0,0

ans = 0
now = 0
while right < N:
    if now <= K:
        now += arr[right]
        right += 1
    else:
        now -= arr[left]
        left += 1
        ans += N - right + 1

while now > K:
    ans += 1
    now -= arr[left]
    left += 1

print(ans)
