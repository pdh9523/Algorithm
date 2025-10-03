from math import sqrt


def is_square(num):
    sq = int(sqrt(num))
    return sq ** 2 == num

def convert(char):
    for i in range(len(char)):
        for j in range(i+1,len(char)+1):
            if is_square(int(char[i:j])):
                return (str(int(char) // (10**(len(char)-j)) +1) + "2"*(len(char)-j))
    return char

N = input()
while True:
    if N != (tmp:=convert(N)):
        N = tmp
    else: break

print(N)