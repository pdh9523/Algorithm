import sys; input = sys.stdin.readline


class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None
        self.prev=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def append(self, data):
        nxt = Node(data)
        if self.head is None:
            self.head = nxt
            self.tail = nxt
        else:
            self.tail.next = nxt
            nxt.prev = self.tail
            self.tail = nxt
        self.size += 1

    def appendleft(self, data):
        prev = Node(data)
        if self.tail is None:
            self.head = prev
            self.tail = prev
        else:
            self.head.prev = prev
            prev.next = self.head
            self.head = prev
        self.size += 1

    def popleft(self):
        if self.head is None:
            return print(-1)
        res = self.head.data
        old_head = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        old_head.next = None
        self.size -= 1
        return print(res)
    
    def pop(self):
        if self.tail is None:
            return print(-1)
        res = self.tail.data
        old_tail = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        old_tail.prev = None
        self.size -= 1
        return print(res)

    def is_empty(self):
        return print(1 if self.head == None and self.tail == None else 0)

    def get_size(self):
        return print(self.size)
    
    def get_tail(self):
        return print(-1 if self.tail is None else self.tail.data)
    
    def get_head(self):
        return print(-1 if self.head is None else self.head.data)
    

q = Queue()
cmd = {
    1: q.appendleft,
    2: q.append,
    3: q.popleft,
    4: q.pop,
    5: q.get_size,
    6: q.is_empty,
    7: q.get_head,
    8: q.get_tail
}
for _ in range(int(input())):
    c, *query = map(int,input().split())
    cmd[c](*query)