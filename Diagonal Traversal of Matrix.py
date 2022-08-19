t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    for i in range(n):
        a.append([int(s) for s in input().split()])
    po=[0]*n
    ne=[0]*n
    for i in range(n):
        for j in range(n):
            if (j-i>=0):
                po[j-i]+=a[i][j]
            else:
                ne[i-j]+=a[i][j]

    for i in range(n-1,-1,-1):
        print(po[i],end=' ')
    for j in range(1,n):
        print(ne[j],end=' ')
    print()
        
