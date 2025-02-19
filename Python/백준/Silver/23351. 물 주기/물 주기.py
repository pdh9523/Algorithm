from heapq import heappop, heappush


N,K,A,B = map(int,input().split())
hq = [K] * N
day = 0
while hq[0] > day:
    for _ in range(A):
        heappush(hq, heappop(hq)+B)
    day += 1
print(day)