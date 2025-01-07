for _ in range(int(input())):
    N,M = map(int,input().split())
    if M>=6: print(0); continue
    
    DP = [[0]*(N+1) for _ in range(M)]
    DP[0][N] = 1
    for i in range(M-1):
        for j in range(N, 1, -1):
            if DP[i][j]:
                
                for k in range(1, int((j-1)**0.5)+1):
                    DP[i+1][k] += DP[i][j]
    print(DP[M-1][1])