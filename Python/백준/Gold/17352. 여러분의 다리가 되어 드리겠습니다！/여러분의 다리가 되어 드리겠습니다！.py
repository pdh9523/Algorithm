import sys; input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b: a,b = b,a
    parents[b] = a

N = int(input())
parents = [*range(N+1)]
for _ in range(N-2):
    union(*map(int,input().split()))

print(*set(map(find, parents[1:])))
