from math import ceil


X,Y,C = map(int,input().split())

if X==0 and Y==0:
    print(0)
else:
    length = X**2 + Y**2
    if length == C**2: 
        print(1)
    elif length > 2 * C**2:
        print(ceil(length**0.5 / C))
    else:
        print(2)