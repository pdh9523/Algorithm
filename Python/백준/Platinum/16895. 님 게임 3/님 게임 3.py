N = int(input())
arr = [*map(int,input().split())]
nim_sum = 0
for a in arr: nim_sum ^= a

ans = 0
for i in range(N):
    for j in range(arr[i]):
        ans += (j ^ nim_sum ^ arr[i] == 0)
print(ans)
