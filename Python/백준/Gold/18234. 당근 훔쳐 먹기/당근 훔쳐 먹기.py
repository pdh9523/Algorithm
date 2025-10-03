import sys; input = sys.stdin.readline


N,T = map(int,input().split())
arr = sorted([[*map(int,input().split())] for _ in range(N)], key=lambda x: x[1])

ans = 0
for i in range(N):
    w,p = arr[i]
    ans += w + (T-N + i) * p
print(ans)