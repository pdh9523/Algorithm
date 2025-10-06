import sys; input = sys.stdin.readline


diff = [0] * 1000002
for _ in range(int(input())):
    a,b = map(int,input().split())
    diff[a] += 1
    diff[b+1] -= 1

arr = [0] * 1000002
now = 0
for i,d in enumerate(diff):
    now += d
    arr[i] = now

input()
for a in map(int,input().split()):
    print(arr[a])
