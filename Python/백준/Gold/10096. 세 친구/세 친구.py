def equal(word1, word2):
    if len(word1) < len(word2):
        word1, word2 = word2, word1
    l,r = 0,0
    res = 0
    while l < len(word1) and r < len(word2):
        if word1[l] == word2[r]:
            l+=1
            r+=1
        else:
            l+=1
            res+=1
        if res > 1: return False
    return True

def check(length, words):
    if length % 2 == 0:
        return "NOT POSSIBLE"
    res = 0
    ans = ""

    left = words[:length//2]; right = words[length//2:]
    if equal(left, right):
        ans = left
        res += 1
    
    left = words[:length//2+1]; right = words[length//2+1:]
    if equal(left, right):
        if ans != right:
            ans = right
            res += 1
    if res == 0:
        return "NOT POSSIBLE"
    elif res == 1:
        return ans
    else:
        return "NOT UNIQUE"

print(check(int(input()), input()))