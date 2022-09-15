t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    b=[0]*(n+1)
    if a[0]==1:
        b[0]=1
    else:
        b[0]=-1
    for i in range(1,n+1):
        if a[i-1]==1:
            b[i]=b[i-1]+1
        else:
            b[i]=b[i-1]-1
    h={}
    for i in range(n+1):
        if b[i] in h:
            h[b[i]]=[h[b[i]][0],i]
        else:
            h[b[i]]=[i,i]
    m=0
    for i in h.values():
        m=max(m,i[1]-i[0])
    print(m)
