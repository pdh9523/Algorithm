import sys; input = sys.stdin.readline


class Node:
    def __init__(self):
        self.child = [None] * 2
        self.count = 0


class Trie:
    def __init__(self, arr, bit_length=26):
        self.values = set()
        self.root = Node()
        self.bit_length = bit_length
        for num in arr: self.insert(num)

    def insert(self, num):
        if num in self.values:
            return len(self.values)
        self.values.add(num)
        
        now = self.root

        for i in range(self.bit_length, -1, -1):
            bit = (num >> i) & 1
            if now.child[bit] is None:
                now.child[bit] = Node()
            now = now.child[bit]
            now.count += 1
        
        return len(self.values)
        
    def find(self, num, is_max):
        now = self.root
        res = 0

        for i in range(self.bit_length, -1, -1):
            bit = (num >> i) & 1 ^ is_max
            
            if now.child[bit] and now.child[bit].count:
                pass
            else:
                bit ^= 1
            now = now.child[bit]            
            res |= (bit << i)
            
        return res

    def remove(self, is_max):
        now = self.root
        res = 0
        for i in range(self.bit_length, -1, -1):
            pref = 1 if is_max else 0
            other = 1 - pref

            bit = pref if now.child[pref] and now.child[pref].count else other
            
            res |= (bit<<i)
            now = now.child[bit]
            
        now = self.root
        for i in range(self.bit_length, -1, -1):
            bit = (res >> i) & 1
            now = now.child[bit]
            now.count -= 1
        
        self.values.discard(res)

        return res
    
    def cmd(self, num, q):
        query = {
            1: self.find_min,
            2: self.find_max,
            3: self.add,
            4: self.remove_min,
            5: self.remove_max
        }
        return query[num](*q)
    
    def find_min(self, v):
        return print(v ^ self.find(v, is_max=False))

    def find_max(self, v):
        return print(v ^ self.find(v, is_max=True))
    
    def add(self, num):
        return print(self.insert(num))
    
    def remove_min(self):
        return print(self.remove(is_max=False))

    def remove_max(self):
        return print(self.remove(is_max=True))
            

def solve():
    N,Q = map(int,input().split())
    trie = Trie(map(int,input().split()))
    for _ in range(Q):
        cmd,*q = map(int,input().split())
        trie.cmd(cmd, q)
    
for _ in range(int(input())): solve()