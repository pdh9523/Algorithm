N = int(input())

arr = [*map(int,input().split())]
prefix_sum = [arr[0]]

for i in range(1,N):
    prefix_sum.append(prefix_sum[-1]+arr[i])

ans = 0
for i in range(1, N-1):
    v = prefix_sum[-1] - prefix_sum[i]

    start = 0
    end = i-1

    if start == end:
        if prefix_sum[0] < v < prefix_sum[i] - prefix_sum[0]: ans += 1
        continue

    check = 0
    while start <= end:
        mid = (start+end) // 2
        if prefix_sum[mid] < v < prefix_sum[i] - prefix_sum[mid]:
            ans += mid + 1 - check
            start = mid + 1
            check = start
        else:
            end = mid - 1

print(ans)