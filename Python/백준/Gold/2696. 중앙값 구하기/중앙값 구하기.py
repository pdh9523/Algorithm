import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def solve():
    N = int(input())
    upper_hq = []
    lower_hq = []
    arr = []
    for _ in range(N//10 + 1): arr.extend(map(int,input().split()))
    cnt = 0
    print((N+1)//2)
    for num in arr:
        heappush(upper_hq, num)
        while len(upper_hq) - len(lower_hq) > 1:
            heappush(lower_hq, -heappop(upper_hq))
        while lower_hq and upper_hq and -lower_hq[0] > upper_hq[0]:
            a,b = -heappop(lower_hq), heappop(upper_hq)
            heappush(lower_hq, -b)
            heappush(upper_hq, a)
        cnt += 1
        if cnt % 2:
            print(upper_hq[0], end=" ")
        if cnt == 20:
            print()
    print()

for _ in range(int(input())):
    solve()