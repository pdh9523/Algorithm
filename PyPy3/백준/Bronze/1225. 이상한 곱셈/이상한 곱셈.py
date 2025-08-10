a,b = input().split()

ans = 0
for x in a:
    for y in b:
        ans += int(x)*int(y)
print(ans)