import sys; input = sys.stdin.readline

def calc(a,b,c):
    if a > b: b += N
    return arr[b] + max(0, (c - arr[a] + rot - 1) // rot) * rot

N,M = map(int,input().split())
arr = [*map(int,input().split())]

rot = sum(arr)

arr = [0,0] + arr + arr
for i in range(3, N*2+2):
    arr[i] += arr[i-1]

ans = 0
for _ in range(M):
    ans = max(ans, calc(*map(int,input().split())))
print(ans)
