from functools import lru_cache

@lru_cache(maxsize=None)
def backtrack(idx=0, prev=-1):
    if idx == length:
        return prev

    result = float('inf')
    for i in range(idx, length):
        cur = int(N[idx:i+1])
        if cur > prev:
            result = min(result, backtrack(i+1, cur))
    return result

N = input()
length = len(N)

last = backtrack()

res = []
idx = 0
prev = -1
while idx < length:
    best = None
    best_next = None

    for i in range(idx, length):
        cur = N[idx:i+1]
        if int(cur) > prev:
            next_idx = i + 1
            if backtrack(next_idx, int(cur)) == last:
                if best is None or int(cur) > int(best):
                    best = cur
                    best_next = next_idx

    res.append(best)
    prev = int(best)
    idx = best_next

print(*res, sep=",")
