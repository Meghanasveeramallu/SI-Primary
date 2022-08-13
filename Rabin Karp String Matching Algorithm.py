def rabin(a,b):
    k=10**9 + 7
    ha=0
    hb=0
    m=len(b)
    n=len(a)
    count=0
    p=73
    p1=p
    for i in range(m):
        hb=(hb+(ord(b[i])-97)*p1)%k
        ha=(ha+(ord(a[i])-97)*p1)%k
        p1=(p1*p)%k
    if (ha==hb):
        count+=1
    p2=p
    for i in range(m,n):
        ha=((ha+(ord(a[i])-97)*p1)%k - ((ord(a[i-m])-97)*p2)%k +k) %k
        hb=(hb*73)%k
        if (ha==hb):
            count+=1
        p1=(p1*p)%k
        p2=(p2*p)%k
    return count

t=int(input())
for i in range(t):
    b,a=map(str,input().split())
    if len(b)<=len(a):
        print(rabin(a,b))
    else:
        print("0")
