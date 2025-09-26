import sys; input = sys.stdin.readline
from heapq import heappop, heappush, heapify


N = int(input())
arr = [0] + [*map(int,input().split())]
hq = [(arr[i], i) for i in range(1,N+1)]
heapify(hq)

for _ in range(int(input())):
    c, *q = map(int,input().split())
    if c == 2:
        while arr[hq[0][1]] != hq[0][0]:
            heappop(hq)
        print(hq[0][1])
    else:
        i,v = q
        heappush(hq, (v,i))
        arr[i] = v