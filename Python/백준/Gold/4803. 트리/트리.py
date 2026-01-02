import sys; input = lambda: sys.stdin.readline().rstrip()


def find(x):
    if parents[x] != x:
        x = find(parents[x])
    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a > b:
        a,b = b,a
    if a == b:
        visit.add(a)
    parents[b] = a

tc = 0
while (tmp:=input()) != "0 0":
    tc += 1

    N,M = map(int,tmp.split())

    parents = [*range(N+1)]

    visit = set()
    for _ in range(M):
        union(*map(int,input().split()))
    visit = set(find(x) for x in visit)

    cnt = 0
    for i in range(1,N+1):
        x = find(i)
        if x not in visit:
            cnt += 1
            visit.add(x)
    ans = ""
    if cnt == 1:
        ans = "There is one tree."
    elif cnt > 1:
        ans = f"A forest of {cnt} trees."
    else:
        ans = "No trees."
    
    print(f"Case {tc}: {ans}")