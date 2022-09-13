# Sequence: Static Array

class Static_Array:
    def __init__(self): # O(1)
        self.A = []
        self.size = 0

    def __len__(self): # O(1)
        return self.size

    def __iter__(self): # O(n)
        yield from self.A

    def build(self, X): # O(n)
        self.A = [x for x in X]
        self.size = len(X)

    def get_at(self,i): # O(1)
        if not (0 <= i < self.size):
            raise IndexError
        return self.A[i]

    def set_at(self,i,x): # O(1)
        if not (0 <= i < self.size):
            raise IndexError
        self.A[i] = x

    def insert_at(self,i,x): # O(n)
        if not (0 <= i <= self.size):
            raise IndexError
        new_list = [None] * (self.size + 1) # O(n+1)

        for j in range(i): # O(i)
            new_list[j] = self.A[j]

        new_list[i] = x # O(1)

        for j in range(self.size - i): # O(n-i)
            new_list[i+j+1] = self.A[i+j]

        self.size += 1
        self.A = new_list # O(1)

    def delete_at(self, i): # O(n)
        if not (0 <= i < self.size):
            raise IndexError
        new_list = [None] * (self.size-1)
        for j in range(i):
            new_list[j] = self.A[j]
        for j in range(self.size - i - 1):
            new_list[i+j] = self.A[i+j+1]
        removed_element = self.A[i]
        self.size -= 1
        self.A = new_list
        return removed_element
        
    def delete_first(self): self.delete_at(0)               # O(n)
    def delete_last(self): self.delete_at(self.size-1)      # O(n)
    def insert_first(self,x): self.insert_at(0,x)           # O(n)
    def insert_last(self,x): self.insert_at(self.size,x)    # O(n)