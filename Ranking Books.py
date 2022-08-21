def f(a,b,n,m):
    c=list(dict.fromkeys(a))
    n=len(c)
    k=n-1
    r=n+1
    for i in range(m):
        for j in range(k,-1,-1):
            #print(b,c,i,j,r,k)
            if b[i]>=c[j]:
                r=j+1
                k=j
            else:
                break
        print(r,end=' ')
    print()
            
t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    m=int(input())
    b=[int(s) for s in input().split()]
    f(a,b,n,m)
