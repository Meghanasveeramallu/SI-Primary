def f(a,n):
    if n==1:
        return a[0]
    p=[-1]*n
    q=[n]*n
    s=[]
    for i in range(0,n):
        while(len(s)>0 and a[i]<a[s[-1]]):
            q[s[-1]]=i
            s.pop()
        s.append(i)
    for i in range(n-1,-1,-1):
        while(len(s)>0 and a[i]<a[s[-1]]):
            p[s[-1]]=i
            s.pop()
        s.append(i)
    ans=0
    for i in range(n):
        ans=max(ans,(q[i]-p[i]-1)*a[i])
    return (ans)

t=int(input())
for k in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    print(f(a,n))
