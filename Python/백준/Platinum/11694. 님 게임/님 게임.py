N = int(input())
arr = [*map(int,input().split())]

if all(x==1 for x in arr):
    exit(print("koosaga" if N%2==0 else "cubelover"))

n = 0
for a in arr:
    n ^= a
print("koosaga" if n else "cubelover")