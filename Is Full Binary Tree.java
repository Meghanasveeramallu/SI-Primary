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

def isFullTree(root):
    if root is None:   
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return (isFullTree(root.left) and isFullTree(root.right))
    return False

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    root=Node(a[0])
    for i in range(1,n):
        root = insert(root,a[i])
    print(isFullTree(root))
