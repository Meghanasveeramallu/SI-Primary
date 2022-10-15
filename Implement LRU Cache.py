t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=[int(s) for s in input().split()]
    b=[]
    h={}
    for i in range(n):
        if a[i] in h:
            b.remove(a[i])
        else:
            if len(b)==k:
                d=b.pop(0)
                del h[d]
        b.append(a[i])
        h[a[i]]=len(b)-1
    for i in range(len(b)):
        print(b[i],end=' ')
    print()
