def get_prime_number(num):
    is_prime = [True] * (num+1)

    for i in range(2, num+1):
        if is_prime[i]:
            for j in range(i*2, num+1, i):
                is_prime[j] = False
            
    return [i for i in range(2,num+1) if is_prime[i]]

LIMIT = 100000
prime = [*map(str,reversed(get_prime_number(LIMIT)))]
while (N:=input()) != "0":
    for p in prime:
        if p in N:
            print(p)
            break