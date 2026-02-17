def C(n, k):
    if k < 0 or k > n or n < 0:
        return 0
    return fact[n] * inv_v[k] % MOD * inv_v[n-k] % MOD

MOD = 5000011

N, K = map(int,input().split())

max_v = N + K + 1
fact = [1] * (max_v + 1)
for i in range(1, max_v + 1):
    fact[i] = fact[i-1] * i % MOD

inv_v = [1] * (max_v + 1)
inv_v[max_v] = pow(fact[max_v], MOD - 2, MOD)
for i in range(max_v - 1, -1, -1):
    inv_v[i] = inv_v[i+1] * (i+1) % MOD

ans = 0
max_B = (N + K) // (K + 1)
for B in range(max_B + 1):
    n_choose = N - B * K + K
    ans = (ans + C(n_choose, B)) % MOD

print(ans)
