t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(((1<<(x+y))-(1<<y))%1000000007)
