import sys; input = sys.stdin.readline


def is_friday(now): return now % 7 == 4

def check():
    DP = [False] * 7
    DP[0] = True
    for a in arr:
        tmp = set()
        for i in range(7):
            if DP[i]:
                tmp.add((a+i)%7)
                if is_friday(a+i): return True
        for x in tmp:
            DP[x] = True
    return False

N = int(input())
arr = [*map(lambda x: int(x)%7,input().split())]

print("YES" if check() else "NO")