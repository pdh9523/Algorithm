from bisect import bisect_right


def make_hansu(dif, idx=0, now=0):
    global hansu
    if idx == len(str(N)) + 1: return
    if now > 0:
        hansu.add(now)
    for i in range(10):
        if now == 0 or now%10 - i == dif:
            make_hansu(dif, idx+1, now*10+i)
    
N = int(input())
hansu = set()
for i in range(-9, 10):
    make_hansu(i)

hansu = sorted(hansu)

print(bisect_right(hansu, N))
