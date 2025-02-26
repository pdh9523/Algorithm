import sys; input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y: return

    if root_x < root_y: 
        root_x,root_y = root_y,root_x

    parent[root_x] = root_y

G = int(input())
parent = [*range(G+1)]

P = int(input())
planes = [int(input()) for _ in range(P)]

ans = 0
for plane in planes:
    x = find(plane)
    if x == 0: break
    union(x, x-1)
    ans += 1

print(ans)