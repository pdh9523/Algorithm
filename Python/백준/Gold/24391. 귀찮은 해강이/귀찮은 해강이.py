import sys; input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N,M = map(int,input().split())
parent = [*range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    union(a,b)
lecture = iter(map(int,input().split()))

now = find(next(lecture))
ans = 0
for _ in range(N-1):
    if now != (nxt:=find(next(lecture))):
        ans += 1
        now = nxt
print(ans)