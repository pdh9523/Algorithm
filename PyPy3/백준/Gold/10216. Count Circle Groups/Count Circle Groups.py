import sys; input = sys.stdin.readline
from itertools import combinations


def solve():
    def is_overlap(x,y):
        x1,y1,d1 = arr[x]
        x2,y2,d2 = arr[y]

        return (x2-x1)**2 + (y2-y1)**2 <= (d1+d2)**2

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(x,y):
        x = find(x)
        y = find(y)
        if x!=y:
            x,y = min(x,y),max(x,y)
            parents[x] = y
        
    N = int(input())
    arr = [[*map(int,input().split())] for _ in range(N)]
    parents = [*range(N)]

    for i,j in combinations(range(N), 2):
        if find(i) != find(j):
            if is_overlap(i,j): union(i,j)
    
    for i in range(N):
        find(i)
    
    print(len(set(parents)))

for _ in range(int(input())):
    solve()