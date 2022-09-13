# Set: Direct Access Array

class Direct_Access_Array:
    def __init__(self): # O(1)
        self.A = []
        self.size = 0

    def __len__(self): # O(1)
        return self.size

    def __iter__(self): # O(u)
        yield from self.A

    def build(self, X): # O(u)
        self.A = [None] * max(X)
        for x in X:
            self.A[x] = x

    def find(self,k): # O(1)
        return self.A[k]

    def insert(self, x): # O(1)
        self.A[x] = x

    def delete(self, k): # O(1)
        self.A[k] = None
        return k
            
    def find_min(self): # O(u)
        min_val = self.A[0]
        for x in self.A:
            if x < min_val:
                min_val = x
        return min_val

    def find_max(self): # O(u)
        max_val = self.A[0]
        for x in self.A:
            if x > max_val:
                max_val = x
        return max_val

    def find_next(self, k): # O(u)
        pass

    def find_prev(self, k): # O(u)
        pass