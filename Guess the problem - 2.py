def f(a,b):
    r=''
    b=b%26
    for i in range(len(a)):
        k=0
        if ord(a[i])+b>122:
            k-=26
        r+=chr(ord(a[i])+b+k)
    return r

t=int(input())
for i in range(t):
    a,b=map(str,input().split())
    b=int(b)
    print(f(a,b))
