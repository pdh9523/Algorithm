import sys; input = sys.stdin.readline

def min(a,b):
    if a[1] > b[1]: return b
    else: return a

def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
    else:
        mid = (start+end) // 2
        tree[idx] = min(init(start,mid, idx*2), init(mid+1, end, idx*2+1))

    return tree[idx]

def find(start, end, left, right, idx):
    if start>right or end<left: return (float('inf'), float('inf'))
    if start>=left and end<=right: return tree[idx]
    mid = (start+end) // 2
    return min(find(start,mid,left,right,idx*2), find(mid+1,end,left,right,idx*2+1))

def update(start,end, data, idx, new_idx):
    if start>new_idx or end<new_idx: 
        return (float('inf'), float('inf'))
    
    if start==end: 
        tree[idx] = data
        return

    mid = (start+end) // 2
    update(start, mid,  data, idx*2, new_idx)
    update(mid+1, end, data, idx*2+1, new_idx)

    tree[idx] = min(tree[idx*2], tree[idx*2+1])

N = int(input())
arr = [*enumerate(map(int,input().split()), start=1)]
tree = [0]*4*N
init(0, N-1, 1)

for _ in range(int(input())):
    a,b,c = map(int,input().split())
    # a 가 1이면 b를 c로 바꾼다.
    if a == 1:
        arr[b-1] = (b, c)
        update(0,N-1, arr[b-1], 1, b-1)
        
    # a 가 2면 b부터 c까지 중 가장 작은 값의 "인덱스"를 출력한다.
    else:
        print(find(0,N-1, b-1, c-1, 1)[0])