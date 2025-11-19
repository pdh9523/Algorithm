import sys; input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left, bisect_right


N,Q = map(int,input().split())
word = input()
reds, blues = [], []
for idx, char in enumerate(word):
    if char == "R": reds.append(idx)
    elif char == "B": blues.append(idx)

for _ in range(Q):
    a,b = map(int,input().split())
    l = bisect_left(reds, a)
    r = bisect_right(blues, b)
    ans = reds[l:l+2] + blues[r-2:r]
    if len(ans) < 4 or ans[1] > ans[2] :
        print(-1)
    else:
        print(*ans)
