N = int(input())
if N == 1: exit(print(0))

arr = sorted(map(int,input().split()))
for _ in range(N): arr.pop()

max_v = arr.pop()
for _ in range(N-1):
    min_v = arr.pop()

print(max_v-min_v)