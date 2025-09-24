def calc_odd(num):
    cnt = 0
    for i in num:
        cnt += int(i) % 2
    return cnt

def recur(num, cnt=0):
    global min_v, max_v
    cnt += calc_odd(num)

    if len(num) == 1:
        max_v = max(max_v, cnt)
        min_v = min(min_v, cnt)
    
    if len(num) == 2:
        nxt = str(sum(map(int,list(num))))
        recur(nxt, cnt)

    for i in range(1, len(num)-1):
        for j in range(i+1, len(num)):
            nxt = str(sum(map(int,(num[:i],num[i:j],num[j:]))))
            recur(nxt, cnt)

min_v = float('inf')
max_v = 0
recur(input())
print(min_v, max_v)