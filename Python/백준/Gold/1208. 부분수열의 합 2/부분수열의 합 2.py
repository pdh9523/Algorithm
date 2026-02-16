def get_subset_sums(nums):
    res = dict()
    for mask in range(1 << len(nums)):
        total = sum(nums[i] for i in range(len(nums)) if mask & (1 << i))
        res[total] = res.get(total, 0) + 1
    return res

N,S = map(int,input().split())
arr = [*map(int,input().split())]

left = arr[:N//2]
right = arr[N//2:]

left_sums = get_subset_sums(arr[:N//2])
right_sums = get_subset_sums(arr[N//2:])

ans = 0
for s, cnt in left_sums.items():
    if S - s in right_sums:
        ans += cnt * right_sums[S - s]

if S == 0: ans -= 1

print(ans)