import sys; input = sys.stdin.readline
from heapq import heappop, heappush

N,K = map(int,input().split())

hq,done = [], []
for x in range(1,N+1):
    i,w = map(int,input().split())
    
    if len(hq) < K:
        heappush(hq, (w,x,i))
    else:
        ww,xx,ii = heappop(hq)
        heappush(hq, (w+ww, xx, i))

        done.append((ww, xx, ii))

ans = 0
for i, r in enumerate(sorted(hq + done, key = lambda x: (x[0], -x[1])), start=1):
    _,_,x = r
    ans += x * i

print(ans)
