N = int(input())
arr = [*map(int,input().split())]
K = int(input())

idx = N // K

for i in range(0, N, idx):
    print(*sorted(arr[i:i+idx]), end=" ")
    