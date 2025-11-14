import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)


def kruskal(size, edges):
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(x,y):
        x = find(x)
        y = find(y)
        if x > y: x,y = y,x
        parents[y] = x
    
    parents = [*range(size+1)]
    edges.sort(key=lambda x:x[2])
    res = 0
    for a,b,c in edges:
        if not find(a) == find(b):
            union(a,b)
            res += c
    return res

N,M = map(int,input().split())
edges = [[*map(int,input().split())] for _ in range(M)]
print(kruskal(N, edges))