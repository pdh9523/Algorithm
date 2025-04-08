not_zero = set()
alphabets = [0] * 10
for _ in range(int(input())):
    num = input()
    not_zero.add(ord(num[0])-ord("A"))
    
    for idx, char in enumerate(num):
        alphabets[ord(char)-ord("A")] += 10**(len(num)-idx-1)

res = sorted(enumerate(alphabets),key=lambda x:-x[1])
if res[-1][0] in not_zero:
    for x in range(9, -1, -1):
        if res[x][0] in not_zero: continue
        res.append(res.pop(x))
        break

ans = 0
k = 9
for idx, value in res:
    ans += k*value
    k -= 1

print(ans)