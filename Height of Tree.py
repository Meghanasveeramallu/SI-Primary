class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def height(root):
    if root is None:
        return -1 
    else :
        l = height(root.left)
        r = height(root.right)
        if (l > r):
            return l+1
        else:
            return r+1

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    root=Node(a[0])
    for i in range(1,n):
        root = insert(root,a[i])
    print(height(root))
