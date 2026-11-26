import sys; input = sys.stdin.readline

SIZE = 5
def calc(arr):
    max_v = 0
    for i in range(SIZE-2):
        for j in range(i+1, SIZE-1):
            for k in range(j+1, SIZE):
                max_v = max(max_v, (arr[i] + arr[j] + arr[k])%10)
    return max_v

arr = [calc([*map(int,input().split())]) for _ in range(int(input()))]
print(max(enumerate(arr, start=1), key=lambda x: (x[1], x[0]))[0])
