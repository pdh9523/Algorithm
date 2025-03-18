group = input()
password = input()
length = len(group)
data = {group[i]: i+1 for i in range(len(group))}

ans = 0
for i in range(len(password)):
    ans *= length
    ans += data[password[i]]
    ans %= 900528
print(ans)