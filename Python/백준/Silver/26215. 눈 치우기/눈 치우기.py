from heapq import heappop, heappush, heapify


N = int(input())
hq = [*map(lambda x: -int(x),input().split())]
heapify(hq)

cnt = 0
while hq:
    if len(hq) >= 2:
        a = heappop(hq)
        b = heappop(hq)
        a += 1
        b += 1
        if a: heappush(hq, a)
        if b: heappush(hq, b)
    else:
        a = heappop(hq)
        a += 1
        if a: heappush(hq, a)
    cnt += 1

if cnt > 1440:
    cnt = -1

print(cnt)