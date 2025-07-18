class Trie:
    class Node:
        def __init__(self):
            self.child = [None, None]
            self.is_end = False

    def __init__(self):
        self.root = self.Node()
    
    def check(self, now):
        for i in range(2):
            if now.child[i]:
                if now.child[i].is_end:
                    return False
                else: 
                    return self.check(now.child[i])
        return True

    def insert(self, now, depth, res=""):
        if depth == 0:
            if self.check(now):
                now.is_end = True
                return res
            return None
        
        for i in range(2):
            if now.child[i] is None:
                now.child[i] = self.Node()
            
            if not now.child[i].is_end:
                result = self.insert(now.child[i], depth-1, res+str(i))
                if result is not None:
                    return result 
        return None

    def search(self, now, res=""):
        global ans
        for i in range(2):
            if now.is_end:
                return ans.append(res)
            if now.child[i]:
                self.search(now.child[i], res+str(i))

N = int(input())
arr = [*map(int,input().split())]

ans = []
trie = Trie()
for x in arr:
    res = trie.insert(trie.root, x)
    if res:
        ans.append(res)
    else:
        exit(print(-1))

print(1)
print(*ans, sep="\n")