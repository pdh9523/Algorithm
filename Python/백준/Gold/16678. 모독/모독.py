import sys; input = sys.stdin.readline

arr = sorted([int(input()) for _ in range(int(input()))])

ans,now = 0,1
for a in arr:
    if a >= now:
        ans += a - now
        now += 1
print(ans)
