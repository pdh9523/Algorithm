import sys; input = sys.stdin.readline

def find(x) -> int:
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y) -> int:
    x = find(x)
    y = find(y)
    if x == y: return
    if x > y: x,y = y,x
    parents[y] = x

    cnts[x] += cnts[y]
    cnts[y] = 0

def counts(x):
    print(cnts[find(x)])

SIZE = 10**6 + 1

cmd = {
    "I": union,
    "Q": counts,
}

parents = [*range(SIZE+1)]
cnts = [1] * (SIZE+1)
for _ in range(int(input())):
    c, *q = input().split()
    q = map(int, q)
    cmd[c](*q)
