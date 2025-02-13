import sys; input = sys.stdin.readline


N = int(input())
day = [0] * 367

for _ in range(N):
    s,e = map(int,input().split())
    day[s] += 1
    day[e+1] -= 1

for i in range(1,367):
    day[i] += day[i-1]

ans = 0
height, width = 0,0
for i in range(1,367):
    if day[i]:
        width += 1
        height = max(height, day[i])
    else:
        ans += width * height
        height, width = 0,0

print(ans)