from math import log2, ceil


N = int(input())

ans = 0 
now = 0
ascending = True
for x in map(int,input().split()):
    if ascending and now < x:
        ascending = False
        ans += 1
    elif not ascending and now > x:
        ascending = True
        ans += 1
    now = x

print(ceil(log2(ans)))