import sys; input = lambda: sys.stdin.readline().rstrip()


trashes = [input() for _ in range(int(input()))]

category = ["P","C","V","S","G","F"]
arr = [*map(int,input().split())]
cost = {category[i]: arr[i] for i in range(6)}
cost["O"] = int(input())
ans = 0
for trash in trashes:
    
    if len(set(list(trash))) == 1:
        ans += min(cost[trash[0]], cost["O"]) * len(trash)
        continue
    
    ans += cost["O"] * len(trash)
print(ans)