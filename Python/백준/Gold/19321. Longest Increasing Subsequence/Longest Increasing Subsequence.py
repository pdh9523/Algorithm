ans = [0]*int(input())
num = 1
for i in sorted(enumerate([*map(int,input().split())]), key=lambda x:(x[1],-x[0])):
    ans[i[0]] = num
    num += 1
print(*ans)