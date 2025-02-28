def f(data, string):
    tmp = ""
    for char in string:
        tmp += data[char]
    return int(tmp)

reversed_data = {str(k):v for k,v in enumerate(input().split())}
data = {v:k for k,v in reversed_data.items()}

ans = 0
for num in input().split():
    ans += f(data, num)
print(f(reversed_data, str(ans)))