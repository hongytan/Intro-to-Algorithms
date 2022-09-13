# Set: Sorted Array

class Sorted_Array:
    def __init__(self): # O(1)
        self.A = []
        self.size = 0

    def __len__(self): # O(1)
        return self.size

    def __iter__(self): # O(n)
        yield from self.A

    def _merge_sort(self, A, a = 0, b = None): 
        if b is None: b = len(A)
        if 1 < b - a:
            c = (a + b + 1) // 2 
            self._merge_sort(A, a, c) 
            self._merge_sort(A, c, b) 
            L, R = A[a:c], A[c:b] 
            self._merge(L, R, A, len(L), len(R), a, b)

    def _merge(self, L, R, A, i, j, a, b):
        if a < b:
            if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
                A[b - 1] = L[i - 1] 
                i = i - 1
            else: 
                A[b - 1] = R[j - 1] 
                j = j - 1
            self._merge(L, R, A, i, j, a, b - 1)

    def build(self, X): # O(nlogn)
        self.A = [x for x in X]         # O(n)
        self.size = len(X)
        self._merge_sort(self.A)        # O(nlogn)

    def _binary_search(self, k, i, j): # O(logn)
        if i >= j: return i
        m = (i+j) // 2
        if k == self.A[m]:
            return m
        elif k < self.A[m]:
            return self._binary_search(k, i, m-1)
        elif k > self.A[m]:
            return self._binary_search(k, m+1, j)

    def find(self,k): # O(logn)
        if len(self) == 0: return None
        i = self._binary_search(k, 0, self.size-1)
        if self.A[i] == k: return k
        else: return None

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
        x = self.A[i]
        self.size -= 1
        self.A = new_list
        return x

    def insert(self, x): # O(n)
        if self.size == 0: self.insert_at(0,x)
        else:
            i = self._binary_search(x, 0, self.size-1)
            if x < self.A[i]:
                self.insert_at(i,x)
            elif x == self.A[i]:
                return False
            else:
                self.insert_at(i+1,x)
        return True

    def delete(self, k): # O(n)
        i = self._binary_search(k, 0, self.size-1)
        assert self.A[i] == k
        return self.delete_at(i)
            
    def find_min(self): # O(1)
        assert self.size != 0
        return self.A[0]

    def find_max(self): # O(1)
        assert self.size != 0
        return self.A[self.size-1]

    def find_next(self, k):
        if self.size == 0:          return None
        i = self._binary_search(k, 0, self.size-1)
        if self.A[i] > k:           return self.A[i]
        if i+1 < self.size:    return self.A[i+1]
        return None

    def find_prev(self, k):
        if self.size == 0: return None
        i = self._binary_search(k, 0, self.size-1)
        if self.A[i] < k: return self.A[i]
        if i > 0: return self.A[i-1]
        return None


A = Sorted_Array()
A.build([123,4,43,43643,12321,665,223,456,1,3589,126,82])
for x in A:
    print(x, end=" | ")
print()
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
# print(A.find_prev(82))
# print(A.find_next(82))
