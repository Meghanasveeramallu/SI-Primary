def c(x,n,num):
    val = (x - pow(num, n))
    if (val == 0):
        return 1
    if (val < 0):
        return 0

    return c(val, n, num + 1) +c(x, n, num + 1)
 
     
t=int(input())
for i in range(t):
    x,n=map(int,input().split())
    print(c(x, n, 1))
