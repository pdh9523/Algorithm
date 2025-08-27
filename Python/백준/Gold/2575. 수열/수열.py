def get_A(num):
    return (num-1) // 3 + 1

def get_B(num):
    if num == 1: return 1
    div = 3
    res = 0
    while num > 2:
        if num % div == 0:
            num //= div
            res += 1
        else:
            div += 1
    return res + (num == 2)

N = int(input())

print(get_A(N), get_B(N))