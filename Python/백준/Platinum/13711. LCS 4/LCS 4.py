from bisect import bisect_left


N = int(input().strip())

data = {num: idx for idx, num in enumerate([*map(int,input().split())])}
arr = [data[num] for num in map(int,input().split())]

lis = []
for idx in arr:
    pos = bisect_left(lis, idx)
    
    if pos < len(lis):
        lis[pos] = idx 
    else:
        lis.append(idx)

print(len(lis))
