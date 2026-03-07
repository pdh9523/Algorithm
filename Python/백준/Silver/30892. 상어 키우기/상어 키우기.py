from heapq import heappop, heappush

N,K,T = map(int,input().split())
arr = sorted(map(int,input().split()))

hq = []
idx = 0
for _ in range(K):
    while idx < N and arr[idx] < T:
        heappush(hq, -arr[idx])
        idx += 1

    if not hq: break

    T -= heappop(hq)
print(T)
