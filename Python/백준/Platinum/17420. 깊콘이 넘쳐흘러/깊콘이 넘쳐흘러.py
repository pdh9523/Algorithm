import sys; input = sys.stdin.readline

N = int(input())
arr = sorted([x for x in zip(map(int,input().split()), map(int,input().split()))], key=lambda x: x[1])

max_v, now = arr[0]
prev = now
ans = 0
for a,b in arr:
    if prev != b:
        now = max(max_v, b)
    prev = b
    if now > a:
        tmp = (now - a - 1) // 30 + 1
        ans += tmp
        a += tmp*30
    max_v = max(max_v, a)

print(ans)
