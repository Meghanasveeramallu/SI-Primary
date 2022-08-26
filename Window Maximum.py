def f(a,n,k):
    s=0
    d=[]
    for i in range(n):
        while (len(d)>0 and a[i]>=a[d[len(d)-1]]):
            d.pop()
        d.append(i)
        if (d[0]==i-k):
            d.pop(0)
        if (i>=k-1):
            s+=a[d[0]]
    return s

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=[int(s) for s in input().split()]
    print(f(a,n,k))
