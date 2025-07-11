def char_to_int(char):
    return ord(char) - ord("a")

def int_to_char(num):
    return chr(num + ord("a"))

def check_max_idx(arr):
    res = -1
    for i in range(len(arr)):
        if arr[i]: res = i
    return res

N = int(input())
word = input()

cnt = [0]*26
for char in word: cnt[char_to_int(char)] += 1

ans = word
check = False
for i in range(N):
    cnt[char_to_int(word[i])] -= 1
    max_char = int_to_char(check_max_idx(cnt))
    if word[i] >= max_char: continue
    for j in range(i+1, N):
        if word[j] == max_char:
            ans = max(ans,word[:i]+word[i:j+1][::-1]+word[j+1:])
        check = True
    if check: break
print(ans)