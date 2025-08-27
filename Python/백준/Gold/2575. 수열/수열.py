# A 문제: 3으로 나눠보기 (왠지는 모르겠는데, 3이 제일 가성비 좋은 것 같음)
# 10 -> 3 3 2 2 // 11 -> 3 3 3 2  // 12 -> 3 3 3 3
# B 문제: 소인수분해 하면서 개수 더하기
def get_A(num):
    case = num % 3
    if case == 1:
        return num // 3 + 1
    if case == 2:
        return num // 3 + 1
    return num // 3 

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
    if num == 2:
        res += 1
    return res

N = int(input())

print(get_A(N), get_B(N))