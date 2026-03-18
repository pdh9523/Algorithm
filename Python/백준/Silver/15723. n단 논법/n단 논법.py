import sys; input = lambda: sys.stdin.readline().rstrip()

def get_index(x):
    return ord(x) - ord('a')

def dfs(start, end):
    if start == end: return True
    for nxt in graph[start]:
        return dfs(nxt, end)
    return False

graph = [[] for _ in range(26)]
for _ in range(int(input())):
    a,b = map(get_index, input().split(" is "))
    graph[a].append(b)

for _ in range(int(input())):
    print("T" if dfs(*map(get_index, input().split(" is "))) else "F")
