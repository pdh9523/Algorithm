N = int(input())
word = input()
stack = []
answers = []
tmp = 0
for i in range(N):
    if word[i] =="(": stack.append(i)
    elif stack:
        tmp = [stack.pop(), i]
        
        while answers and answers[-1][0] > tmp[0]:
            answers.pop()
        
        if answers and answers[-1][1] + 1 == tmp[0]:
            tmp[0] = answers.pop()[0]
        answers.append(tmp)

print(0 if not answers else max(end-start+1 for start,end in answers))