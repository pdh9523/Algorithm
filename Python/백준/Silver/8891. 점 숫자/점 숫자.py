import sys; input = sys.stdin.readline
from bisect import bisect_right

arr = [0, 1]
for i in range(1, 25001):
    arr.append(arr[-1] + i)

def get_xy(v):
    idx = bisect_right(arr, v) - 1
    x = v - arr[idx] + 1
    y = idx - (v - arr[idx])
    return x, y

def get_value(x, y):
    return arr[x + y - 1] + x - 1

for _ in range(int(input())):
    v1, v2 = map(int, input().split())
    x1, y1 = get_xy(v1)
    x2, y2 = get_xy(v2)
    print(get_value(x1 + x2, y1 + y2))
