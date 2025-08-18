from heapq import heappop, heappush


N,K = map(int,input().split())

hq = []
now = 0
for a in map(int,input().split()):
    heappush(hq, a)
    now += a

    while now > K:
        tmp = heappop(hq)
        if now - tmp >= K:
            now -= tmp
        else:
            heappush(hq, tmp)
            break
    
    print(-1 if now < K else len(hq), end=" ")
