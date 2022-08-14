def gcd(x,y):
    while (y):
        temp=y
        y=x%y
        x=temp
    return x

def lcm(x,y):
    g=gcd(x,y)
    return (x*y)//g,g

n=int(input())
for i in range(n):
    a=[int(s) for s in input().split()]
    if (a[0]==0 and a[1]==0):
        print("0 0")
    else:
        p,q=lcm(a[0],a[1])
        print(p,q)
