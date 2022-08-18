def f(a,b,n):
    a.sort()
    b.sort()
    c=0
    i=n-1
    j=i
    while(i>=0 and j>=0):
        if (a[i]>b[j]):
            c+=1
            i-=1
        j-=1
        
    return c
    

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    b=[int(s) for s in input().split()]
    print(f(a,b,n))
