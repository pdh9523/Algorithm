import sys; input = sys.stdin.readline


N = int(input())
tmp = [*map(int,input().split())]
arr = [*enumerate(tmp, start = 1)]
arr.sort(key = lambda x: -x[1])

required_seat = sum(tmp) // 2

DP = dict()
DP[0] = []

ans = 0
for idx, nums in arr:
    for seat in range(required_seat, -1 , -1):
        after = seat + nums
        if seat in DP and after not in DP:

            ans = max(ans, after)

            DP[after] = DP[seat][:]
            DP[after].append(idx)

print(len(DP[ans]))
print(*DP[ans])