import sys; input = lambda: sys.stdin.readline().rstrip()

def count(word):
    res = {k:0 for k in range(10)}
    for char in word:
        if char not in check: continue
        res[check[char]] = res.get(check[char], 0) + 1
    return res

check = {
    "Z": 0,
    "O": 1,
    "W": 2,
    "H": 3,
    "U": 4,
    "F": 5,
    "X": 6,
    "V": 7,
    "G": 8,
    "I": 9,
}

for tc in range(1, int(input())+1):
    counter = count(input())
    counter[3] -= counter[8]
    counter[5] -= counter[4]
    counter[7] -= counter[5]

    counter[9] -= counter[5] + counter[6] + counter[8]
    counter[1] -= counter[0] + counter[2] + counter[4]

    print(f"Case #{tc}: {"".join(str(i) * counter[i] for i in sorted(counter))}")
