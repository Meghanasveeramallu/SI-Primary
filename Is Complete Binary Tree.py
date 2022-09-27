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

def isCompleteBT(root):
    if root is None:
        return True
    queue = []
    flag = False
    queue.append(root)
    while(len(queue) > 0):
        tempNode = queue.pop(0)
        if (tempNode.left):
            if flag == True :
                return "No"
            queue.append(tempNode.left)
        else:
            flag = True
        if(tempNode.right):
            if flag == True:
                return "No"
            queue.append(tempNode.right)
        else:
            flag = True
    return "Yes"

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    root=Node(a[0])
    for i in range(1,n):
        root = insert(root,a[i])
    print(isCompleteBT(root))
