def check(comb):
    res = [arr[c] for c in comb]
    for i in range(L):
        for j in range(L):
            if res[i][j] != res[j][i]: return False
    return res

def backtrack(idx=0, res=[]):
    if len(res) == L:
        if c:= check(res):
            exit(print(*c, sep="\n"))
        return
    
    if idx == N: return
    
    for i in range(N):
        if visit[i]: continue
        if idx > 0 and arr[res[0]][idx] != arr[i][0]: continue

        visit[i] = True
        backtrack(idx+1, res+[i])
        visit[i] = False

L,N = map(int,input().split())
arr = sorted([input() for _ in range(N)])
visit = [False] * N

backtrack()
print("NONE")