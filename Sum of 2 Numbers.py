def f(a,n):
    s=sum(a)
    if s%2!=0:
        return "No"
    m=s//2
    h=set()
    for i in range(n):
        b=m-a[i]
        if a[i] not in h:
            h.add(a[i])
        if b in h:
            return "Yes"
    return "No"
    
t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    print(f(a,n))
