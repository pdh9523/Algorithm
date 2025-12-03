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
kmp = create_kmp(input().split()[::-1])

k = 0
p = 0
sum_v = float('inf')
for i in range(N):
    tk = N-i-1
    tp = i+1-kmp[i]
    if tk + tp < sum_v:
        sum_v = tk+tp
        k,p = tk,tp
print(k,p)
