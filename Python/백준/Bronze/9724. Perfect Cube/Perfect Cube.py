import sys; input = sys.stdin.readline
from bisect import bisect_right

sqs = [x**3 for x in range(1,1260)]
for tc in range(1,int(input())+1):
    a,b = map(int,input().split())
    print(f"Case #{tc}: {bisect_right(sqs, b) - bisect_right(sqs, a-1)}")
