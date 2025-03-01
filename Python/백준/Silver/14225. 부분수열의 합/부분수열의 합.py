from itertools import combinations

data = set()
N = int(input())
arr = [*map(int,input().split())]
for i in range(1,N+1):
    for comb in combinations(arr, i):
        data.add(sum(comb))

for i in range(1,sum(arr)+2):
    if i not in data:
        print(i)
        break
