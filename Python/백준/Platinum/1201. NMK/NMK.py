N,M,K = map(int,input().split())

if N < M+K-1 or N > M*K: exit(print(-1))

ans = [*range(K,0,-1)]
N -= K
M -= 1
while M:
    ans += range(K+N//M,K,-1)
    K += N//M
    N -= N//M
    M -= 1
print(*ans)