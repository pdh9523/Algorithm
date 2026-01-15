# def get_primes(size):
#     primes = [True] * (size + 1)

#     for i in range(2, size+1):
#         if primes[i]:
#             for j in range(i*2, size+1, i):
#                 primes[j] = False
    
#     return set(i for i in range(2,size+1) if primes[i])

# size = 100_000_000
# primes = get_primes(size)

# num = 1
# cnt = 0
# while num:
#     if 6*num + 1 in primes and 12*num + 1 in primes and 18*num + 1 in primes:
#         print(6*num+1, (6*num+1)*(12*num+1)*(18*num+1))
#         cnt += 1
#     num += 1
#     if cnt == 10:
#         break

print(601*1201*1801, 601)