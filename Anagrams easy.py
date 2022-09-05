def f(a,b):
    if len(a)!=len(b):
        return "False"
    p={}
    q={}
    for i in range(len(a)):
        if a[i] in p:
            p[a[i]]+=1
        else:
            p[a[i]]=1
        if b[i] in q:
            q[b[i]]+=1
        else:
            q[b[i]]=1
    if (len(p)!=len(q)):
        return "False"
    r=list(p.keys())
    for i in range(len(r)):
        if r[i] in q:
            if p[r[i]]!=q[r[i]]:
                return "False"
        else:
            return "False"
    return "True"

t=int(input())
for i in range(t):
    a,b=map(str,input().split())
    print(f(a,b))
