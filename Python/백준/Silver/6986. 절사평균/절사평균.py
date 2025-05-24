import sys; input = sys.stdin.readline


N,K = map(int,input().split())
arr = sorted([float(input()) for _ in range(N)])

a_sum = sum(arr[K:N-K])
b_sum = a_sum + arr[K]*K + arr[N-K-1]*K

print(f"{a_sum/(N-(2*K)) + 0.00000001:.2f}")
print(f"{b_sum/N + 0.00000001:.2f}")