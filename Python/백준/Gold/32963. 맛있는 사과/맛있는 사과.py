import sys; input = sys.stdin.readline
from bisect import bisect_left


N,Q = map(int,input().split())

ans = dict()
max_v = 0
cnt = 0
for taste, size in sorted(zip(map(int,input().split()), map(int,input().split())), reverse=True):
    if size > max_v:
        max_v = size
        cnt = 1
    elif size == max_v:
        cnt += 1
    ans[taste] = cnt

b = sorted(ans.keys())
for _ in range(Q):
    i = bisect_left(b, int(input()))
    if i >= len(b):
        print(0)
    else:
        print(ans.get(b[i], 0))
