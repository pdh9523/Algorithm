import sys; input = sys.stdin.readline


N = int(input())
arr = sorted([tuple(map(int,input().split())) for _ in range(N)])

start,end = arr[0]
res = []
jump = end-start
reach = end + jump
for s,e in arr[1:]:
    if s <= end:
        end = max(end, e)
    else:
        jump = end * 2 - start
        reach = max(jump, reach)
        
        if s <= reach:
            start,end = s,e
        else: break

print(end)