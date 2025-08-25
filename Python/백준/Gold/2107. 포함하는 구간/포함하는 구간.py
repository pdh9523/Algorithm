import sys; input = sys.stdin.readline


arr = []
starts = dict()
for i in range(1,int(input())+1):
    a,b = map(int,input().split())
    arr.append((a,i))
    starts[i] = a
    arr.append((b,-i))

arr.sort()
active = set()
data = dict()
for num,idx in arr:
    if idx > 0:
        active.add(idx)
        data[idx] = 0
    if idx < 0:
        active.discard(-idx)
        for x in active:
            if starts[x] < starts[-idx]:
                data[x] += 1
ans = 0
for a in data:
    ans = max(ans, data[a])
print(ans)
