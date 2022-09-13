# Sequence: Dynamic Array

class Dynamic_Array:
    def __init__(self): # O(1)
        self.A = []
        self.size = 0
        self._compute_bounds()
        self._resize(0)
    
    def __len__(self): # O(1)
        return self.size

    def __iter__(self): # O(n)
        yield from self.A[0:self.size]

    def build(self, X): # O(n)
        for x in X: self.insert_last(x)

    def get_at(self,i): # O(1)
        if not (0 <= i < self.size):
            raise IndexError
        return self.A[i]

    def set_at(self,i,x): # O(1)
        if not (0 <= i < self.size):
            raise IndexError
        self.A[i] = x

    def _compute_bounds(self): # O(1)
        self.upper = len(self.A)
        self.lower = len(self.A) // 4

    def _resize(self, n): # O(1) or O(n)
        if (self.lower < n < self.upper): return # O(1)
        m = max(n,1) * 2
        A = [None] * m
        for i in range(self.size):
            A[i] = self.get_at(i)
        self.A = A
        self._compute_bounds()

    def insert_last(self,x): # O(1)
        self._resize(self.size)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):# O(1)
        self.A[self.size] = None
        self.size -= 1
        self._resize(self.size)

    def insert_at(self,i,x): # O(n)
        A = [None] * len(self.A)
        for j in range(i):
            A[j] = self.A[j]
        A[i] = x
        for j in range(self.size - i):
            A[i+j+1] = self.A[i+j]
        self.A = A
        self.size += 1
        self._resize(self.size)

    def delete_at(self,i): # O(n)
        A = [None] * len(self.A)
        for j in range(i):
            A[j] = self.A[j]
        for j in range(self.size - i - 1):
            A[i+j] = self.A[i+j+1]
        self.A = A
        self.size -= 1
        self._resize(self.size)
    
    def delete_first(self): self.delete_at(0)               # O(n)
    def insert_first(self,x): self.insert_at(0,x)           # O(n)