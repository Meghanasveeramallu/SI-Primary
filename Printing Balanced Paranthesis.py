def f(a,n,i,o,c):
    if i==n:
        for k in range(n):
            print(a[k],end='')
        print()
        return
    if (o<n//2):
        a[i]='{'
        f(a,n,i+1,o+1,c)
    if (c<o):
        a[i]='}'
        f(a,n,i+1,o,c+1)
        
t=int(input())
for j in range(t):
    print("Test Case #{}:".format(j+1))
    n=2*int(input())
    a=[' ']*n
    f(a,n,0,0,0)
