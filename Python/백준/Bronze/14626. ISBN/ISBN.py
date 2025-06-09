now = 0
for i, char in enumerate(input()):
    if char == "*": idx = i
    else: now += (3 if i%2 else 1) * int(char)
for i in range(10):
    if (now + i*(3 if idx%2 else 1)) % 10 == 0: 
        print(i); break