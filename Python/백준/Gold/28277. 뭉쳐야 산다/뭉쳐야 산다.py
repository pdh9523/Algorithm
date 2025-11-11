import sys; input = sys.stdin.readline


def get_set(it):
    _, *x = it
    return set(x)

def stl(a,b):
    if len(sets[a]) < len(sets[b]):
        sets[a], sets[b] = sets[b], sets[a]
    sets[a].update(sets[b])
    sets[b].clear()

def sout(x):
    print(len(sets[x]))

N,Q = map(int,input().split())

sets = [None for _ in range(N+1)]
for i in range(1, N+1):
    sets[i] = get_set(map(int,input().split()))

cmd = {
    1: stl,
    2: sout
}

for _ in range(Q):
    a, *q = map(int,input().split())
    cmd[a](*q)