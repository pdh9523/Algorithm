import sys; input = sys.stdin.readline


def calc_digit(num):
    res = 0 
    while num:
        res += num%10
        num //=10
    return res

def check(num):
    while num <= 10**18:
        if calc_digit(num) % 2: return num
        num *= 2

for _ in range(int(input())):
    print(check(int(input())))