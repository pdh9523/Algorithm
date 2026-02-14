import sys; input = sys.stdin.readline

N = int(input())
arr = [float(input()) for _ in range(N)]

now = arr[0]
max_v = arr[0]

for i in range(1, N):
    now = max(arr[i], now * arr[i])
    max_v = max(max_v, now)

print(f"{max_v:.3f}")
