import sys; input = sys.stdin.readline


translate = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
}

N,K = map(int,input().split())
arr = []
for i in range(N,K+1):
    tmp = ""
    for char in str(i):
        tmp += translate[char] + " "
    arr.append((tmp, i))

cnt = 0
for k,v in sorted(arr):
    print(v, end=" ")
    cnt += 1
    if cnt % 10 == 0:
        print()
