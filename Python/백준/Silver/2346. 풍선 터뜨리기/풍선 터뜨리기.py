from collections import*
input()
q=deque(enumerate(map(int,input().split())))
while q:i,v=q.popleft();print(i+1,end=" ");q.rotate(-v+(v>0))