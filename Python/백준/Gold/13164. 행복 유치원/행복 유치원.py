N,K = map(int,input().split())
arr = [*map(int,input().split())]
diff = sorted([arr[i+1] - arr[i] for i in range(N-1)])
print(sum(diff[i] for i in range(N-K)))