import sys; input = sys.stdin.readline

N = int(input())
arr = sorted([[*map(int,input().split())] for _ in range(N)], key=lambda x: -x[1])

now = 1000000
for t,e in arr:
    now = min(now, e)-t

print(now if now > 0 else -1)
