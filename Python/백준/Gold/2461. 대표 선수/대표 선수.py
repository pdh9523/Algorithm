'''
대표 선수

우선순위 큐, 투 포인터

포인터를 기반으로 우선순위 큐를 구현.
'''
import sys; input = sys.stdin.readline
from heapq import heappop, heappush


N,M = map(int,input().split())
arr = [sorted([*map(lambda x: (int(x), i), input().split())]) for i in range(N)]

hq, max_v = [], 0
for i in range(N):
    heappush(hq, arr[i][0])
    max_v = max(max_v, arr[i][0][0])

ans = max_v-hq[0][0]

pointer = {k: 0 for k in range(N)}
while True:
    value, idx = heappop(hq)
    if pointer[idx] == M-1: break

    pointer[idx] += 1
    heappush(hq, (arr[idx][pointer[idx]]))
    max_v = max(max_v, arr[idx][pointer[idx]][0])
    
    ans = min(ans, max_v - hq[0][0])

print(ans)