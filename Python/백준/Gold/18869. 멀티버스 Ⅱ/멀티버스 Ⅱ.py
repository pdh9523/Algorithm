import sys; input = sys.stdin.readline


N,M = map(int,input().split())

data = dict()
for _ in range(N):
    arr = [*map(int,input().split())]
    sorted_arr = sorted(set(arr))
    rank = {sorted_arr[i]:i for i in range(len(sorted_arr))}

    key = tuple([rank[a] for a in arr])
    data[key] = data.get(key, 0) + 1

ans = 0
for k in data:
    v = data[k]
    ans += v * (v-1) // 2

print(ans)