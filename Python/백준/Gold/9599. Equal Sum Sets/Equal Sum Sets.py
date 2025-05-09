import sys; input = sys.stdin.readline


def backtrack(N,res,idx,start=0):
    if res < 0: return
    if idx == 0:
        if res == 0:
            global ans
            ans += 1
        return
    
    for i in range(start+1,N+1):
        backtrack(N,res-i, idx-1, i)

N,M,K = map(int,input().split())
while N and M and K:
    ans = 0
    backtrack(N,K,M)
    print(ans)
    N,M,K = map(int,input().split())