def f(num):
    return int(num**0.5)**2==num
def c(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)+1):
            if f(int(x[i:j])):return c((str(int(x)//(10**(len(x)-j))+1)+"2"*(len(x)-j)))
    return x
print(c(input()))