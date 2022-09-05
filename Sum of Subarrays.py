n=int(input())
a=[int(s) for s in input().split()]
b=[0]*(n+1)
b[0]=0
for i in range(n):
    b[i+1]=b[i]+a[i]
t=int(input())
for i in range(t):
    i,j=map(int,input().split())
    print(b[j+1]-b[i])
