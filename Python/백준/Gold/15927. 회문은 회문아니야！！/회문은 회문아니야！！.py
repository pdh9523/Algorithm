def check(n):
    left = word[:(len(word)-1)//2+1-n]
    right = word[len(word)//2:len(word)-n]
    if left != right[::-1]: return True
    return False

word = input()

if check(0):
    print(len(word))

elif check(1):
    print(len(word) - 1)

else: print(-1)