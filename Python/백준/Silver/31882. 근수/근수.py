def calc(num):
    return num*(num+1)*(num+2) // 6

N = int(input())
word = input()

ans = 0
cnt = 0
for char in word:
    if char == "2":
        cnt += 1
    else:
        ans += calc(cnt)
        cnt = 0
ans += calc(cnt)

print(ans)