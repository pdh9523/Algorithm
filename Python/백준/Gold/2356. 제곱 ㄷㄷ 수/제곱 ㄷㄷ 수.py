from math import isqrt


def is_square(num):
    return isqrt(num) ** 2 == num

def convert(char):
    for i in range(len(char)):
        for j in range(i+1,len(char)+1):
            if is_square(int(char[i:j])):
                return convert((str(int(char) // (10**(len(char)-j))+1) + "2"*(len(char)-j)))
    return char

print(convert(input()))