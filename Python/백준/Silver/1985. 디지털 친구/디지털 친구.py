def switch(l, i, check):
    l[i+1] = str(int(l[i+1]) + 1 * check)
    l[i] = str(int(l[i]) - 1 * check)
    return l

def search(arr, s):
    for idx in range(len(arr)-1):
        for x in -1, 1:
            tmp = switch(arr[:], idx, x)
            if tmp[0] == '0': continue
            stmp = set(tmp)
            if s==stmp and '-1' not in stmp and '10' not in stmp:
                return True
    return False

for _ in range(3):
    a,b = input().split()
    if set(a)==set(b): print("friends")
    else: print("almost friends" if search(list(b), set(a)) or search(list(a), set(b)) else "nothing")
