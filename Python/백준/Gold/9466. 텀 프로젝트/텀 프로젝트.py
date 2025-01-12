'''
텀 프로젝트

DFS

사이클을 이루고 있는지 어떻게 확인할 것인가? 에 관한 문제
사이클을 확인하는 방법에 대해서 더 고민해봐야겠다.
바로 떠오르는 풀이가 시간초과, 메모리초과 연달아 뜨는걸 보니 기초부터 잘못됐다는 생각이 들었다.
'''
import sys; input = sys.stdin.readline
sys.setrecursionlimit(111111)


def solve():
    def dfs(now, depth=1):
        nonlocal ans

        visit[now] = True
        cycle[now] = depth

        nxt = arr[now]
        
        depth += 1
        if visit[nxt]:
            if nxt in cycle:
                ans -= depth - cycle[nxt]
            return

        dfs(nxt, depth)
        
    N = int(input())
    arr = [*map(lambda x: int(x)-1, input().split())]
    visit = [False] * N
    ans = N
    for i in range(N):
        if visit[i]: continue
        cycle = dict()
        dfs(i)

    print(ans)

for _ in range(int(input())):
    solve()