import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    if (x:=find(x)) == (y:=find(y)): return False
    parent[x] = y
    return True

N,M = map(int,input().split())
edges = [[*map(int,input().split())] for _ in range(M)]

parent = [*range(N+1)]
ans = 0
for a,b in edges:
    if union(a,b):
        ans += 1

print(M-ans)