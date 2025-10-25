import sys; input = sys.stdin.readline


arr = [] 
for _ in range(int(input())):
    s,e = input().split()
    arr.append((s,-1))
    arr.append((e,1))
arr.sort()

now = 0
max_v = 0
ans = ""
for d,i in arr:
    now -= i
    if now > max_v:
        ans = d
        max_v = now

print(ans)