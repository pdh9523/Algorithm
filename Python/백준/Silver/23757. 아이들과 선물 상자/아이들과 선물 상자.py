from heapq import heappop, heappush, heapify

def check():
    for a in arr:
        x = -heappop(hq)
        if (rest := x-a) < 0: return False
        heappush(hq, -rest)
    return True

N,M = map(int,input().split())
hq = [*map(lambda x: -int(x), input().split())]
heapify(hq)

arr = [*map(int,input().split())]

print(int(check()))
