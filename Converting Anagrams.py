def f(a,b):
    c=[0]*26
    d=[0]*26
    e=0
    for i in range(len(a)):
        c[ord(a[i])-97]+=1
    for i in range(len(b)):
        d[ord(b[i])-97]+=1
    for i in range(26):
        if c[i]!=d[i]:
            e+=abs(c[i]-d[i])
    return e


t=int(input())
for i in range(t):
    a,b=map(str,input().split())
    print(f(a,b))
