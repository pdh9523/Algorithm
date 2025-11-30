def create_kmp(word):
    size = len(word)
    kmp = [0]*size
    i = 0
    for j in range(1, size):
        while i and word[i] != word[j]:
            i = kmp[i-1]
        if word[i] == word[j]:
            i += 1
            kmp[j] = i
    return kmp

N = int(input())
word = input()

kmp = create_kmp(word)
print(N-kmp[-1])
