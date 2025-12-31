import sys; input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        x = find(parent[x])    
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        global ans
        ans += 1
        return
    
    if x > y:
        x,y = y,x
    parent[y] = x

N,M = map(int,input().split())

parent = [*range(N+1)]

ans = 0
for _ in range(M):
    a,b = map(int,input().split())
    union(a,b)

tmp = set()
tmp.add(1)

for i in range(1,N+1):
    if find(i) not in tmp:
        ans += 1
        tmp.add(find(i))

print(ans)