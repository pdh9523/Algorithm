def min_dist(x):
    return min(abs(x - a) for a in arr)

N = int(input())
arr = sorted(map(int,input().split()))
s,e = map(int,input().split())

ans = []

first_odd = s if s % 2 else s + 1
last_odd = e if e % 2 else e - 1
if first_odd <= e: ans.append(first_odd)
if last_odd >= s: ans.append(last_odd)

for i in range(N - 1):
    mid = (arr[i] + arr[i+1]) // 2
    for d in -1, 0, 1:
        tmp = mid + d
        if tmp % 2 and s <= tmp <= e:
            ans.append(tmp)

print(max(ans, key=min_dist))