import sys; input = sys.stdin.readline


ans = []
end = -1
start = -1
cost = float('inf')
for s,e,c in sorted([[*map(int,input().split())] for _ in range(int(input()))]):
    if end < s:
        if end != -1:
            ans.append((start,end,cost))
        start = s
        cost = float('inf')
    end = max(e, end)
    cost = min(cost, c)

ans.append((start,end,cost))

print(len(ans))
for a in ans:
    print(*a)
