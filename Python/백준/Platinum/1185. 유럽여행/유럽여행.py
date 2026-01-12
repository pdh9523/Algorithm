import sys; input = sys.stdin.readline

def mst_kruskal(size, edges):
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
arr = [0] * (N+1)
start = -1
tmp = float('inf')
for i in range(1,N+1):
    c = int(input())
    if c < tmp:
        start = i
        tmp = c
    arr[i] = c

edges = []
for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append([a,b,2*c+arr[a]+arr[b]])

print(mst_kruskal(N, edges) + arr[start])
