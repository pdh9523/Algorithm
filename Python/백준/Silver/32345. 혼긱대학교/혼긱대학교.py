import sys; input = lambda: sys.stdin.readline().rstrip()

MOD = 1000000007
check = "aeiou"

def calc(*arg):
    res = 1
    for a in arg:
        res = (res * a) % MOD
    return res

def solve():
    word = input()
    DP = []
    cnt = 0
    for char in word:
        if char in check:
            DP.append(cnt+1)
            cnt = 0
        else:
            cnt += 1
    
    return -1 if len(DP) < 1 else calc(*DP[1:])

for _ in range(int(input())):
    print(solve())
