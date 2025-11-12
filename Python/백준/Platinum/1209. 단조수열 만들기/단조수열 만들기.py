import sys; input = sys.stdin.readline
from heapq import heappop, heappush


def slope_trick(arr):
    hq = []
    ans = []
    for i, x in enumerate(arr):
        for _ in range(2):
            heappush(hq, -x)
        heappop(hq)
        ans.append(-hq[0])

    for i in range(N-2, -1, -1):
        ans[i] = min(ans[i], ans[i+1])

    return (sum(abs(ans[i] - arr[i]) for i in range(N)))

N = int(input())
arr = [int(input()) for _ in range(N)]
print(min(slope_trick(arr), slope_trick(arr[::-1])))