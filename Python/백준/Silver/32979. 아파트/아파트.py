from collections import deque


N = int(input())
T = int(input())
arr = deque([*map(int,input().split())])

nums = [*map(int,input().split())]
ans = []
for num in nums:
    for _ in range(num-1):
        arr.append(arr.popleft())
    ans.append(arr[0])
print(*ans)