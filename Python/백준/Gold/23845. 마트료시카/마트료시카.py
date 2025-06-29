N = int(input())

cnt = [0] * 100001
for i in map(int,input().split()):
    cnt[i] += 1

ans = 0
for i in range(100000, 0, -1):
    while cnt[i]:
        j = i
        while cnt[j]:
            cnt[j] -= 1 
            j-=1
        ans += i * (i-j)

print(ans)