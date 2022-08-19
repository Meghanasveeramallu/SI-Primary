def power(a,n):
    if n==0:
        return 1
    if a==0:
        return 0
    x=power(a,n//2)
    if (n&1)==0:
        return (x*x)%1000000007
    else:
        return (((a*x)%1000000007)*x)%1000000007

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    a=a%1000000007
    print(power(a,b))
