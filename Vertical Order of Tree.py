from collections import OrderedDict

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
    def insert(self,root, key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root
    
    def f(self,root,v,hm):
        if root is None:
            return
        if v not in hm:
            hm[v] = []
        hm[v].append(root.val)
        global minl
        minl=min(v,minl)
        global maxl
        maxl=max(v,maxl)
        self.f(root.left,v-1,hm)
        self.f(root.right,v+1,hm)
        
t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    r=Node(a[0])
    for i in range(1,n):
        r=r.insert(r,a[i])
    minl=0
    maxl=-1
    hm={}
    r.f(r,0,hm)
    for i in range(minl,maxl+1):
        hm[i].sort()
        for j in hm[i]:
            print(j,end=' ')
        print()
    print()
