N = int(input())
arr = [*map(int,input().split())]
stack = []

for a in arr:
    stack.append(a)
    while len(stack) >= 2 and (stack[-1] + stack[-2]) % 2 == 0:
        for _ in range(2):
            stack.pop()

print(len(stack))
