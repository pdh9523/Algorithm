def get_A(num):
    if num == 1: return "1 1"
    res = (num-1) // 3 + 1
    check = num%3==1
    return f"{res} {res-check}"

def get_B(num):
    if num == 1: return "1 1"
    div = 2
    res = 0
    check = 0
    while num >= div:
        if num % div == 0:
            if div == 2:
                check += 1
            num //= div
            res += 1
        else:
            div += 1

    return f"{res} {res - check//2}"

N = int(input())
print(get_A(N), get_B(N))