from heapq import heappop, heappush


N,M = map(int,input().split())
data = dict()
arr = [*map(int,input().split())]
left,right = 0,0
hq = []
while right < 2*M-1 :
    if arr[right] not in data:
        heappush(hq, -arr[right])
    data[arr[right]] = data.get(arr[right], 0) + 1
    right += 1

while right < N:
    print(-hq[0], end=" ")
    
    data[arr[left]] -= 1
    if data[arr[left]] == 0 :
        data.pop(arr[left])
    
    if arr[right] not in data:
        heappush(hq, -arr[right])
    data[arr[right]] = data.get(arr[right], 0) + 1

    while -hq[0] not in data:
        heappop(hq)

    left += 1
    right += 1
print(-hq[0], end=" ")