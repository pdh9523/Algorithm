Av,As,Ae = map(int,input().split())
Bv,Bs,Be = map(int,input().split())
Cv,Cs,Ce = map(int,input().split())

limit = Av * Bv * Cv
while Ae <= limit and Be <= limit and Ce <= limit:
    s = max(As,Bs,Cs)
    e = min(Ae,Be,Ce)

    if s <= e:
        exit(print(s))
    if Ae <= Be and Ae <= Ce:
        As += Av
        Ae += Av
    elif Be <= Ae and Be <= Ce:
        Bs += Bv
        Be += Bv
    else:
        Cs += Cv
        Ce += Cv
print(-1)
