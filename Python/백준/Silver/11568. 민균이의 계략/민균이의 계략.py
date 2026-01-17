from bisect import bisect_left

N = int(input())
arr = [*map(int,input().split())]

DP = [arr[0]]
for a in arr:
    if a > DP[-1]:
        DP.append(a)
    else:
        DP[bisect_left(DP, a)] = a

print(len(DP))