from math import ceil


arr = sorted(enumerate(map(int,input().split())), key=lambda x: -x[1])
times = [0]+[*map(lambda x: int(x)*30,input().split())]

l = 25000 - int(input()) * 100

ans = 0
for k,v in arr:
    if k==0:
        ans += ceil(l / v)
        l = 0
    else:
        exp = min(times[k]*v, l)
        ans += ceil(exp / v)
        l -= exp
    
    if l == 0:
        break
print(ans)
