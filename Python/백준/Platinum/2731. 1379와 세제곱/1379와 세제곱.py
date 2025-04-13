def get_number(num_str):
    res = 0
    for idx, n in enumerate(num_str[::-1]):
        target = int(n)
        power = 10 ** idx
        for k in range(10):
            nxt = res + k * power
            if nxt ** 3 // power % 10 == target:
                res = nxt
                break
    return res

for _ in range(int(input())):
    print(get_number(input()))