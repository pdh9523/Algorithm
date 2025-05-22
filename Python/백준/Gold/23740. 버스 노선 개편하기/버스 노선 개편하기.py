import sys; input = sys.stdin.readline


arr = sorted([[*map(int,input().split())] for _ in range(int(input()))])
start,end,cost = arr[0]

ans = []
for s,e,c in arr:
    if end < s:
        ans.append((start,end,cost))
        start = s
        cost = float('inf')
    end = max(e, end)
    cost = min(cost, c)

ans.append((start,end,cost))

print(len(ans))
for a in ans:
    print(*a)
