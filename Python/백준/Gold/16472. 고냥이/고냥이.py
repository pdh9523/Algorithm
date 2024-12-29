N = int(input())
word = input()

left, right = 0,0
data = dict()
ans = 0
while right < len(word):
    if len(data) < N or data.get(word[right]):
        data[word[right]] = data.get(word[right], 0) + 1
        right += 1
        ans = max(ans, right-left)
    else:
        data[word[left]] -= 1
        if not data[word[left]]: data.pop(word[left])
        left += 1
print(ans)
