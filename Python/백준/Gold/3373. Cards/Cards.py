import sys; input = sys.stdin.readline


N = int(input())
arr = sorted([sorted([*map(int,input().split())]) for _ in range(N)], key=sum)

ans = 0
for i in range(N//2):
    ans -= arr[N-1-i][1]
    ans += arr[i][0]

print(ans)