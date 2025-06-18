import sys; input = sys.stdin.readline
from math import log2

N = int(input())
arr = [0] * 63
for a in map(int,input().split()):
    if a == 0: continue
    arr[int(log2(a))] += 1

for i in range(62):
    arr[i+1] += arr[i] // 2

for i in range(62,-1,-1):
    if arr[i]: exit(print(2**i))