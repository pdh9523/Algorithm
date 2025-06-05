import sys; input = sys.stdin.readline


N = int(input())
arr = iter(sorted([tuple(map(int,input().split())) for _ in range(N)]))

start,end = next(arr)
res = []
jump = end-start
reach = end + jump
for s,e in arr:
    if s <= end:
        end = max(end, e)
    else:
        jump = end * 2 - start
        reach = max(jump, reach)
        
        if s <= reach:
            start,end = s,e
        else: break

print(end)