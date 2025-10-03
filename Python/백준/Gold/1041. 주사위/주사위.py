def calc(size):
    if size == 1: return sum(dice)-max(dice)
    
    l = size-2
    return ((4*l+5*l**2)*min_one) + ((8*l+4)*min_two) + (4*min_three)

two = [(0,1), (0,2), (0,3), (0,4), (1,5), (2,5), (3,5), (4,5), (1,2), (2,4), (3,4), (1,3)]
three = [(0,1,2), (0,1,3), (0,2,4), (0,3,4), (5,1,2), (5,1,3), (5,2,4), (5,3,4)]

N = int(input())
dice = [*map(int,input().split())]

min_one = min(dice)
min_two = min([dice[x]+dice[y] for x,y in two])
min_three = min([dice[x]+dice[y]+dice[z] for x,y,z in three])
print(calc(N))