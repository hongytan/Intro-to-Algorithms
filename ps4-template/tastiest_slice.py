from Set_AVL_Tree import BST_Node, Set_AVL_Tree

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        
        # Sum
        A.sum = A.item.val
        if A.right: A.sum += A.right.sum
        if A.left: A.sum += A.left.sum

        # Max Prefix
        left = -float('inf')
        right = -float('inf')
        middle = A.item.val
        if A.left: 
            left = A.left.max_prefix
            middle += A.left.sum
        if A.right: 
            right = middle + A.right.max_prefix
        A.max_prefix = max(left,middle,right)

        # Max Prefix Key
        if A.max_prefix == middle:
            A.max_prefix_key = A.item.key
        elif A.max_prefix == left:
            A.max_prefix_key = A.left.max_prefix_key
        else:
            A.max_prefix_key = A.right.max_prefix_key

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)

    def max_prefix(self):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        k, s = 0, 0
        k = self.root.max_prefix_key
        s = self.root.max_prefix
        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing 
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice 
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0
    toppings.sort(key = lambda toppings: toppings[0]) # O(nlogn)
    for (x,y,t) in toppings:
        B.insert(Key_Val_Item(y,t))
        (Y_, T_) = B.max_prefix()
        if T_ > T:
            X, Y, T = x, Y_, T_

    return (X, Y, T)

tastiest_slice([(-7, 8, 5), (2, -4, 3), (7, 10, -1), (4, -3, 9), (-5, 1, 9)])