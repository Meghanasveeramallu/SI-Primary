t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    n = 0
    n = ((1 << x) | n)
    n = ((1 << y) | n)
    print(n%1000000007)
   
