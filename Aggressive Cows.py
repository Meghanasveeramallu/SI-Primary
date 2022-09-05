def possible(a,m,k):
    c=1
    last=a[0]
    for i in range(1,n):
        if a[i]-last>=m:
            c+=1
            last=a[i]
            if (c>=k):
                return True
    return False

def f(a,n):
    a.sort()
    l=1
    h=a[n-1]-a[0]
    r=0
    while(l<=h):
        m=(l+h)//2
        if (possible(a,m,k)):
            r=m
            l=m+1
        else:
            h=m-1
    return r

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=[int(s) for s in input().split()]
    print(f(a,n))
