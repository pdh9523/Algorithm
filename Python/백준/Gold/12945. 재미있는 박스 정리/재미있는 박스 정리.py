import sys; input = sys.stdin.readline


N = int(input())
arr = sorted([int(input()) for _ in range(N)])

left = 0
right = (N-1) // 2 + 1
ans = 0
while right < N:
    while right < N and arr[left] * 2 <= arr[right]:
        left += 1
        right += 1
        ans += 1
    else:
        right += 1
        ans += 1

remains = (N-1) // 2 + 1 - left + N - right

print(ans + remains)
