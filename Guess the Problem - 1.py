def f(a,b):
    s=set()
    r=''
    for i in range(len(a)):
        s.add(a[i])
    for i in range(len(b)):
        if b[i] not in s:
            r+=b[i]
    return r

t=int(input())
for i in range(t):
    a,b=map(str,input().split())
    print(f(a,b))
