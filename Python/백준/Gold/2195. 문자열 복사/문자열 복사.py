data = dict()

s = input()
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        tmp = s[i:j]
        data.setdefault(len(tmp), set()).add(tmp)

t = input()
ans = 0
start = 0 
while start < len(t):
    for end in range(len(t), start, -1):
        if t[start:end] in data.setdefault(end-start, set()):
            start = end
            ans += 1
            break

print(ans)
