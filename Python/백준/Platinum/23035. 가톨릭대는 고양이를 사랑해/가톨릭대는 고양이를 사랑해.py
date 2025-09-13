import sys; input = sys.stdin.readline


def binary_search(pos):
    start,end = 0, len(DP)-1

    while start <= end:
        mid = (start+end) // 2
        if compare(DP[mid], pos):
            start = mid + 1
        else:
            end = mid - 1
    return start

def compare(a,b):
    return a[0] <= b[0] and a[1] <= b[1]

size = [*map(int,input().split())]
arr = sorted([pos for _ in range(int(input())) if compare((pos:=[*map(int,input().split())]), size)])

DP = []
for pos in arr:
    if not DP or compare(DP[-1], pos):
        DP.append(pos)
    else:
        DP[binary_search(pos)] = pos

print(len(DP))