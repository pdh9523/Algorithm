from heapq import heappop,heappush


N = int(input())
arr = [*map(int, input().split())]

hq = []
ans = []
for i, x in enumerate(arr):
    for _ in range(2):
        heappush(hq, -(x-i))
    heappop(hq)
    ans.append(-hq[0])

for i in range(N-2, -1, -1):
    ans[i] = min(ans[i], ans[i+1])

print(*[ans[i]+i for i in range(N)])
