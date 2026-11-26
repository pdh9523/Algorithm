def char_to_num(char):
    return ord(char) - ord("A")

def num_to_char(num):
    return chr(num + ord("A"))

def calc(word):
    ret = 0
    for i in range(1,len(word)):
        if word[i] > word[i-1]: ret += 1
        else: ret -= 1
    return abs(ret) <= 1

def backtrack(word, bit):
    global ans
    if len(word) > len(ans): return
    
    if calc(word):
        ans = word
        return

    for i in range(26):
        if bit & (1<<i): continue
        backtrack(word + num_to_char(i), bit|(1<<i))

N = int(input())
word = input()

bit = 0
for char in word:
    bit |= (1<<char_to_num(char))

ans = "AAAAAAAAAA"
backtrack(word, bit)

print(len(ans))
print(ans)