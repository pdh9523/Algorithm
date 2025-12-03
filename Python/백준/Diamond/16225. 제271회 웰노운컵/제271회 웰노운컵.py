from heapq import heappop, heappush


N = int(input())
arr = sorted([a for a in zip(map(int,input().split()), map(int,input().split()))], key=lambda x: x[1])

ans = arr[0][0]
hq = []
for i in range(2,N-1,2):
    heappush(hq, -arr[i-1][0])
    heappush(hq, -arr[i][0])

    ans += -heappop(hq)

print(ans)