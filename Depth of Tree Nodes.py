class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.dep = -1
        
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

h={}
def depth(root,d):
    if(root==None):
        return 
    root.dep = d
    h[root.val]=root.dep
    depth(root.left, d+1);
    depth(root.right, d+1);

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    root=Node(a[0])
    for i in range(1,n):
        root = insert(root,a[i])
    depth(root,0)
    for i in range(n):
        print(h[a[i]],end=' ')
    print()
