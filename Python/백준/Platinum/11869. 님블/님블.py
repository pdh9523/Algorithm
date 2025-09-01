input()
nim_sum = 0
for a in map(int,input().split()): nim_sum ^= a
print("koosaga" if nim_sum else "cubelover")