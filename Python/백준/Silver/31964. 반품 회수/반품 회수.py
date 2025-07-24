N = int(input())
arr = [*zip((x:=[*map(int,input().split())]), map(int,input().split()))]

max_v = max(x)
ans = 0
for a,b in arr:
    ans = max(ans, max(max_v+max_v-a, b) + a)
print(ans)