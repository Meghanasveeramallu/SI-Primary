def f(a, n):
    maxi=1
    for i in range(n-1):
        b=set()
        b.add(a[i])
        mn=a[i]
        mx=a[i]
        for j in range(i+1,n):
            if a[j] in b:
                break
            b.add(a[j])
            mn=min(mn,a[j])
            mx=max(mx,a[j])
            if ((mx-mn)==j-i):
                maxi=max(maxi,mx-mn+1)
    return maxi

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    print(f(a,n))
