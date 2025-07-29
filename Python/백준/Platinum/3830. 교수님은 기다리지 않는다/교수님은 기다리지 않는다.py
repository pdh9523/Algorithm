import sys; input= sys.stdin.readline; sys.setrecursionlimit(10**6)


def union(x,y,w):
    value[x] -= w
    parent[x] = y
    parent_value[x] = value[y]

def find(x):
    if parent[x] != x:
        p,v = parent[x], parent_value[x]
        parent[x] = find(p)
        value[x] += value[p] - v
        parent_value[x] = value[parent[x]]
    return parent[x]

def measure(x,y,w):
    if find(x) != find(y):
        union(parent[x], parent[y], w+value[x]-value[y])

def ask(a,b):
    print(value[b]-value[a] if find(a) == find(b) else "UNKNOWN")

command = {
    "!": measure,
    "?": ask
}
while True:
    N,M = map(int,input().split())
    if N==M==0:break

    parent = [*range(N+1)]
    value = [0]*(N+1)
    parent_value = [0]*(N+1)

    for _ in range(M):
        cmd, *query = input().split()
        command[cmd](*map(int,query))