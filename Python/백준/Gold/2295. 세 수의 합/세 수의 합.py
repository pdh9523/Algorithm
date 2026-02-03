import sys; input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])
sum_set = set(x+y for x in arr for y in arr)

for i in range(N-1, -1, -1):
    for j in range(i+1):
        if arr[i] - arr[j] in sum_set:
            exit(print(arr[i]))
