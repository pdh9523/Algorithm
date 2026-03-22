from collections import Counter

S = Counter(input())
T = Counter(input())

def check():
    for t in T:
        if T.get(t, 0) > S.get(t, 0):
            return "NEED FIX"
    return "OK"

print(check())
