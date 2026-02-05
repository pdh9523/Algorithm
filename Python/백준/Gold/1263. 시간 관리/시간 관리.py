import sys; input = sys.stdin.readline

N = int(input())
arr = sorted([[*map(int,input().split())] for _ in range(N)], key=lambda x: -x[1])

now = float('inf')
for t,e in arr:
    now = min(now-t, e-t)

print(now if now > 0 else -1)
