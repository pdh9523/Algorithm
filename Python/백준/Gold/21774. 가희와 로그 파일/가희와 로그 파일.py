import sys; input = lambda: sys.stdin.readline().strip()
from bisect import bisect_left, bisect_right


N,Q = map(int,input().split())

data = [[] for _ in range(7)]
for _ in range(N):
    a,b = input().split("#")
    data[int(b)].append(a)

for _ in range(Q):
    start, end, level = input().split("#")
    ans = 0
    for i in range(int(level), 7):
        ans += (bisect_right(data[i], end) - bisect_left(data[i], start))
    print(ans)
