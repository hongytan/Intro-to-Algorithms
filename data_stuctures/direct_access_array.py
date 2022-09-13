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
        self.size = max(X)+1
        self.A = [None] * self.size
        
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
        min_val = self.size * 2
        for x in self.A:
            if x:
                if x < min_val:
                    min_val = x
        return min_val

    def find_max(self): # O(u)
        max_val = -1
        for x in self.A:
            if x:
                if x > max_val:
                    max_val = x
        return max_val

    def find_next(self, k): # O(u)
        first = False
        candidate = -1
        for x in self.A:
            if not first:
                if x:
                    if x > k:
                        first = True
                        candidate = x
            else:
                if x:
                    if k < x < candidate:
                        candidate = x
        if candidate == -1: return None
        else: return candidate

    def find_prev(self, k): # O(u)
        first = False
        candidate = -1
        for x in self.A:
            if not first:
                if x:
                    if x < k:
                        first = True
                        candidate = x
            else:
                if x:
                    if candidate < x < k:
                        candidate = x
        if candidate == -1: return None
        else: return candidate


# A = Direct_Access_Array()
# A.build([123,4,43,43643,12321,665,223,456,1,3589,126,82])
# for x in A:
#     print(x, end=" | ")
# print()
# print(len(A))
# print(A.find(53))
# A.insert(53)
# for x in A:
#     print(x, end=" | ")
# print()
# print(A.find(53))
# print(A.delete(53))
# for x in A:
#     print(x, end=" | ")
# print()
# print(A.find_min())
# print(A.find_max())
# print(A.find_prev(153))
# print(A.find_next(167))