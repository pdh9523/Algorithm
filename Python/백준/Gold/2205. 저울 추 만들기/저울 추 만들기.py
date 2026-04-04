def get(num):
    x = 0
    while True:
        if 2**x <= num < 2**(x+1):
            return 2**(x+1)
        x+=1

N = int(input())
visit = [False] * (N+1)
ans = [0] * (N+1)

now = get(N)
for i in range(N, 0, -1):
    if now-i > N or visit[now-i]:
        now = get(i)
    ans[i] = now-i
    visit[now-i] = True

for i in range(1,N+1):
    print(ans[i])
