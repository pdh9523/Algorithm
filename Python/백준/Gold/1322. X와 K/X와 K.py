X,K = map(int,input().split())

ans = 0
for i in range(64):
    if not ((X>>i)&1):
        if K&1:
            ans |= 1<<i
        K >>= 1
        if K == 0: break

print(ans)
