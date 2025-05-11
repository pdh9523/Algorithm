def buy_one(n):
    res = arr[n] * B
    arr[n] = 0
    return res

def buy_two(n):
    tmp = min(arr[n], arr[n+1])
    res = tmp * (B+C)
    arr[n] -= tmp
    arr[n+1] -= tmp
    return res

def buy_three(n):
    tmp = min(arr[n], arr[n+1], arr[n+2])
    res = tmp * (B+2*C)
    arr[n] -= tmp
    arr[n+1] -= tmp
    arr[n+2] -= tmp
    return res

N,B,C = map(int,input().split())
arr = [*map(int,input().split())] + [0,0]

ans = 0
if B < C:
    print(sum(arr)*B)
else:
    for i in range(N):
        if arr[i+1] > arr[i+2]:
            x = min(arr[i], arr[i+1]-arr[i+2])
            arr[i] -= x
            arr[i+1] -= x

            ans += (B+C) * x
            ans += buy_three(i)
            ans += buy_one(i)
        else:
            ans += buy_three(i)
            ans += buy_two(i)
            ans += buy_one(i)
    print(ans)