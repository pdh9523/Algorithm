import sys; input = lambda: sys.stdin.readline().rstrip()

def check():
    for i in range(len(ring)):
        for j in range(len(word)):
            if ring[(i+j)%len(ring)] != word[j]:
                break
        else:
            return True
    return False

word = input()
ans = 0
for _ in range(int(input())):
    ring = input()
    ans += check()

print(ans)
