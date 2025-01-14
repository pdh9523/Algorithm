'''
사냥꾼

이분 탐색

x축 좌표를 기반으로 동물과 가장 가까운 사로를 찾고, 
거리를 구해 잡을 수 있는지 계산한다.
절대값으로 주어지기 때문에, 가장 가까운 값을 구하려면 왼쪽 값과 오른쪽 값 모두를 비교해야한다.
'''
import sys; input = sys.stdin.readline


def binary_search(x):
    idx, left, right = 0, 0, M-1
    while left <= right:
        mid = (left+right) // 2

        if lines[mid] == x: return mid
        
        if lines[mid] < x:
            idx = mid
            left = mid + 1
        else:
            right = mid - 1
    return idx


M,N,L = map(int,input().split())
lines = sorted([*map(int,input().split())])

ans = 0
for _ in range(N):
    x,y = map(int,input().split())

    idx = binary_search(x)
    dist_left = abs(x - lines[idx]) + y
    dist_right = abs(x - lines[idx+1]) + y if idx < M-1 else float('inf')

    dist = min(dist_left, dist_right)
    ans += dist<=L

print(ans)