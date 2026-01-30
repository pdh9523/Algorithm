from itertools import permutations

def check(x):
    res = float('inf')
    for p in ps:
        res = min(res, sum(abs(arr[p[i]][0] - dr[i][0] * x) + abs(arr[p[i]][1] - dr[i][1] * x) for i in range(4)))
    return res

def ternary_search():
    left,right = 1, 2_000_000_000

    while right - left >= 3:
        left_mid = (left * 2 + right) // 3
        right_mid = (left + right * 2) // 3
        if check(left_mid/2) < check(right_mid/2):
            right = right_mid
        else:
            left = left_mid
    return left, right

dr = (1,1),(1,-1),(-1,1),(-1,-1)
ps = [*permutations(range(4))]

arr = [[*map(int,input().split())] for _ in range(4)]

start,end = ternary_search()

ans = 0
min_v = float('inf')
for i in range(start, end+1):
    now = check(i/2)
    if min_v > now or abs(min_v - now) < 1e-9:
        ans = i
        min_v = now
print(ans)
