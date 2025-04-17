'''
현수막 걸기

정렬, 이분탐색?

1. 말뚝 중 두개를 골라, 두 말뚝 사이의 공간이 현수막의 밑변이 되도록
2. 적절한 깃대를 골라, 두 말뚝 정중앙에 깃대의 길이가 현수막의 높이가 되도록 삼각형
'''
import sys; input = sys.stdin.readline


def check(p, idx):
    s = p * polls[idx] * 0.5
    if s <= R:
        return s
    return 0

N,M,R = map(int,input().split())
pos = sorted([*map(int,input().split())])
polls = sorted([*map(int,input().split())])

widths = set()
for i in range(N):
    for j in range(i+1,N):
        widths.add(pos[j]-pos[i])

ans = -1
for w in widths:
    left, right = 0, M-1
    while left <= right:
        mid = (left+right) // 2
        if tmp:=check(w,mid):
            ans = max(tmp, ans)
            left = mid + 1
        else:
            right = mid - 1

print(ans)