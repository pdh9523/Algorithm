import sys; input = sys.stdin.readline


N,M = map(int,input().split())

xs,ys = [],[]
for _ in range(M):
    x,y = map(int,input().split())
    xs.append(x)
    ys.append(y)

xs.sort(); ys.sort()

mid = M//2
mx = xs[mid] if M%2 else (xs[mid-1]+xs[mid]) // 2
my = ys[mid] if M%2 else (ys[mid-1]+ys[mid]) // 2

ans = 0
for i in range(M):
    ans += abs(mx-xs[i]) + abs(my-ys[i])
print(ans)