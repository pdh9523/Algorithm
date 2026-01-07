import sys; input = sys.stdin.readline


def make(x,y):
    graph[x].append(y)
    graph[y].append(x)

def find(x):
    if parents[x] != x:
        x = find(parents[x])
    return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)
    
    if x > y: x,y = y,x

    parents[y] = x

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
parents = [*range(N+1)]

cmd = {
    "E": make,
    "F": union
}

for _ in range(M):
    a,b,c = input().split()
    cmd[a](int(b),int(c))

for i in range(1,N+1):
    if len(graph[i]) > 1:
        for j in range(1, len(graph[i])):
            union(graph[i][j], graph[i][j-1])

ans = 0
for i in range(1,N+1):
    if parents[i] == i:
        ans += 1
print(ans)
