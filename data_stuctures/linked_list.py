# Sequence: Linked List

class Node:
    def __init__(self, x):
        self.item = x
        self.next = None

    def later_node(self,i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i-1)

class Linked_List:
    def __init__(self): # O(1)
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self): # O(1)
        return self.size

    def __iter__(self): # O(n)
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X): # O(n)
        tmp_node = Node(None)
            
        for i in range(len(X)):
            if i == 0:
                self.head = Node(X[i])
                tmp_node = self.head
            else:
                node = Node(X[i])
                tmp_node.next = node
                tmp_node = node
        self.tail = tmp_node
        self.size = len(X)

    def get_at(self,i): # O(n)
        if not (0 <= i < self.size):
            raise IndexError
        node = self.head.later_node(i)
        return node.item

    def set_at(self,i,x): # O(n)
        if not (0 <= i < self.size):
            raise IndexError
        node = self.head.later_node(i)
        node.item = x

    def insert_at(self,i,x): # O(n)
        if not (0 <= i <= self.size):
            raise IndexError

        node = Node(x)

        if i == 0:
            node.next = self.head
            self.head = node
        elif i == self.size:
            self.tail.next = node
            self.tail = node
        else:
            prev_node = self.head.later_node(i-1)
            node.next = prev_node.next
            prev_node.next = node
        
        self.size += 1

    def delete_at(self, i): # O(n)
        if not (0 <= i < self.size):
            raise IndexError

        if i == 0:
            x = self.head.item
            self.head = self.head.next
        elif i == self.size-1:
            x = self.tail.item
            node = self.head.later_node(i-1)
            self.tail = node
            node.next = None
        else:
            node = self.head.later_node(i-1)
            x = node.next.item
            node.next = node.next.next

        self.size -= 1
        return x
        
    def delete_first(self): self.delete_at(0)             # O(1)
    def delete_last(self): self.delete_at(self.size-1)    # O(n)
    def insert_first(self,x): self.insert_at(0,x)         # O(1)
    def insert_last(self,x): self.insert_at(self.size, x) # O(1)