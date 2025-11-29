from heapq import heappop, heappush


N = int(input())
arr = [*map(int,input().split())]

hq = []
for i, v in enumerate(arr):
    heappush(hq, (-v, i, 1))

min_v = min(arr)
ans = -hq[0][0] - min_v
for _ in range(int(input())):
    now, idx, cnt = heappop(hq)

    cnt += 1
    new = arr[idx] / cnt
    heappush(hq, (-new, idx, cnt))

    min_v = min(min_v, new)
    ans = min(ans, -hq[0][0]-min_v)

print(ans)
