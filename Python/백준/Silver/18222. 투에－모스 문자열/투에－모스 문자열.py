def dvcq(x):
    if x <= 1: return x
    return 1-dvcq(x//2) if x%2 else dvcq(x//2)

print(dvcq(int(input())-1))