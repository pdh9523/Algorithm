stack = []
for char in input():
    if char == ")" and stack and stack[-1] == "(" : stack.pop()
    else: stack.append(char)

print(len(stack))
