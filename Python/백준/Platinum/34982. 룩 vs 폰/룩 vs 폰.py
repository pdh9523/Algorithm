N, M, K = map(int,input().split())

if M <= N: print(1)
elif N == 1: print(2)
elif N == 2:
    if K == 3: print(4)
    else: print(3)
else: print(5)
