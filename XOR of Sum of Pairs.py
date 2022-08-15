def XORsum(arr, n):     
    xoR = 0;
    for i in range (0, n) :
        xoR = xoR ^ arr[i]
    return xoR * 2

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    print(XORsum(a,n))
