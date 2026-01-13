import sys; input = sys.stdin.readline


def create_pi(word):
    length = len(word)
    pi = [0]*length
    j = 0
    for i in range(1, length):
        while word[i] != word[j] and j > 0:
            j = pi[j-1]

        if word[i] == word[j]:
            j += 1
            pi[i] = j
    return pi

def find(word, compare):
    res,i,j = 0,0,0
    while i < len(compare):
        if compare[i] == word[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = pi[j-1]

        if j == len(word):
            res += 1
            j = pi[j-1]

    return res

N = int(input())
arr = input().split()
brr = (brr:=input().split()) + brr[:-1]

pi = create_pi(arr)
ans = find(arr,brr)

div = 2
while ans >= div and N >= div:
    while ans%div==0 and N%div==0:
        ans//=div
        N//=div
    div+=1
print(f"{ans}/{N}")