s = input()

ans = 0
t = ""
for c in input():
    t += c
    if t not in s:
        t = c
        ans += 1

print(ans + int(bool(t)))