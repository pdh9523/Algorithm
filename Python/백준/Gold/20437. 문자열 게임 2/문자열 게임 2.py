import sys; input = lambda: sys.stdin.readline().rstrip()


for _ in range(int(input())) :
    word = input()
    K = int(input())

    data = dict()
    for i in range(len(word)) :
        data.setdefault(word[i], list()).append(i)

    max_v = -1
    min_v = float('inf')
    for res in data.values():
        for i in range(len(res)-K+1):
            max_v = max(max_v, res[i+K-1] - res[i] + 1)
            min_v = min(min_v, res[i+K-1] - res[i] + 1)

    if max_v == -1 or min_v == float('inf'):
        print(-1)
    else:
        print(min_v, max_v)
