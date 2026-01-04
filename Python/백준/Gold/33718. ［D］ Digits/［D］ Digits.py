import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)


def add(a, b):
    return [(a + b, f"{a} + {b} = {a + b}")]

def sub(a, b):
    res = []
    if a - b > 0:
        res.append((a - b, f"{a} - {b} = {a - b}"))
    if b - a > 0:
        res.append((b - a, f"{b} - {a} = {b - a}"))
    return res

def mul(a, b):
    return [(a * b, f"{a} * {b} = {a * b}")]

def div(a, b):
    res = []
    if b != 0 and a % b == 0:
        q = a // b
        if q > 0:
            res.append((q, f"{a} / {b} = {q}"))
    if a != 0 and b % a == 0:
        q = b // a
        if q > 0:
            res.append((q, f"{b} / {a} = {q}"))
    return res

OPS = (add, sub, mul, div)

def backtrack(state, steps):
    key = tuple(sorted(state))
    if key in visit:
        return None
    visit.add(key)

    if T in state:
        return steps

    if len(state) == 1:
        return steps if state[0] == T else None

    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = state[i], state[j]
            rest = [state[k] for k in range(n) if k not in (i, j)]

            seen_values = set()
            for op in OPS:
                for val, expr in op(a, b):
                    if val <= 0 or val in seen_values:
                        continue
                    seen_values.add(val)
                    res = backtrack(rest + [val], steps + [expr])
                    if res is not None:
                        return res
    return None

T = int(input())
arr = [*map(int, input().split())]

if T in arr:
    exit(print(0))

visit = set()
answer = backtrack(arr, [])

if answer:
    print(len(answer))
    print(*answer, sep="\n")
else: print(-1)
