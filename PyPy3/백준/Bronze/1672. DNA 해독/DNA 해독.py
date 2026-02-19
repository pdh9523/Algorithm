DNA = "AGCT"
table = [[0,2,0,1],
         [2,1,3,0],
         [0,3,2,1],
         [1,0,1,3]]

seq = {k:i for i,k in enumerate(DNA)}

N = int(input())
word = [seq[x] for x in input()]

while len(word) > 1:
    word.append(table[word.pop()][word.pop()])

print(DNA[word[0]])
