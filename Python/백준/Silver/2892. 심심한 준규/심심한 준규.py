input()
ans = ""
for c in input().split():
    ans += "." if int(c, 16) < 64 else "-"
print(ans)