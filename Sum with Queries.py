t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    m=int(input())
    s=sum(a)
    for j in range(m):
        i,j,x=map(int,input().split())
        s+=(j-i+1)*x
    print(s)
