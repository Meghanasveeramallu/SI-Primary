def check(x):
    return (x and (x & (x-1))==0)
  
def f(a, n):
    if (n == 1):
        if check(a[0]):
            return "YES"
    t = 0
    for i in range(0, 32):
        t = t | (1 << i)
    for i in range(0, 32):
        ans = t
        for j in range(0, n):
            if (a[j] & (1 << i)):
                ans = ans & a[j]
        if (check(ans)):
            return "YES"
    return "NO"

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    print(f(a,n))
