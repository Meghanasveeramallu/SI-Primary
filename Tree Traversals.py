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

def ino(root):
    if root:
        ino(root.left)
        print(root.val,end=' ')
        ino(root.right)

def pre(root):
    if root:
        print(root.val,end=' ')
        pre(root.left)
        pre(root.right)

def post(root):
    if root:
        post(root.left)
        post(root.right)
        print(root.val,end=' ')

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    root=Node(a[0])
    for i in range(1,n):
        root = insert(root,a[i])
    pre(root)
    print()
    ino(root)
    print()
    post(root)
    print()
    print()
