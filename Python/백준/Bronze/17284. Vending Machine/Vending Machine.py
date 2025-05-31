cash = 5000
costs = [0, 500, 800, 1000]
for i in map(int,input().split()):
    cash -= costs[i]
print(cash)