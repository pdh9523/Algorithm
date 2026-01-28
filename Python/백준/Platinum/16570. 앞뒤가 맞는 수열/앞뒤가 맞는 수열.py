def kmp(word):
    size = len(word)
    pi = [0]*size
    i = 0
    for j in range(1, size):
        while i and word[i] != word[j]:
            i = pi[i-1]
        if word[i] == word[j]:
            i += 1
            pi[j] = i
    return pi

N = int(input())
arr = kmp(input().split()[::-1])

max_v = -1
cnt = 0
for a in arr:
    if max_v < a:
        max_v = a
        cnt = 1
    elif max_v == a:
        cnt += 1

if max_v == 0: print(-1)
else: print(max_v, cnt)
