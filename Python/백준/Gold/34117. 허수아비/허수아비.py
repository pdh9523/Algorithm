from heapq import heappop, heappush


N,K = map(int,input().split())

hq = []
now = 0
for a in map(int,input().split()):
    heappush(hq, a)
    now += a

    while len(hq) > 1 and now > K:
        now -= heappop(hq)
    
    print(-1 if now < K else len(hq), end=" ")
