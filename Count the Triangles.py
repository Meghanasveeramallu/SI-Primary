def count(a,n):
    a.sort()
    c=0
    for i in range(n - 1, 0, -1):
        l = 0
        r = i - 1
        while(l < r):
            if(a[l] + a[r] > a[i]):
                c += r - l
                r -= 1
            else:
                l += 1
    return c

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    print(count(a,n))
