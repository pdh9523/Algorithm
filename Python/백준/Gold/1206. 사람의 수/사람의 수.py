def check(num, mul):
    return num * mul % 100000000 == 0 or int((num+99999)*mul/100000000) - int(num*mul/100000000) >= 1

N = int(input())
arr = [int(input().split(".")[1])*100000 for _ in range(N)]
for mul in range(1, 1001):
    if all(check(arr[i], mul) for i in range(N)): exit(print(mul))