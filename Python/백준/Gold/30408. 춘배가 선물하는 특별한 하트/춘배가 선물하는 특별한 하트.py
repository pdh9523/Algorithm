N,M = map(int,input().split())
visit = set()

def dfs(now):
    if now in visit:
        return
    
    if M == now:
        exit(print("YES"))
    
    if now < M:
        return
    visit.add(now)
    dfs(now // 2)
    if now % 2 :
        dfs(now // 2 + 1)

dfs(N)
print("NO")