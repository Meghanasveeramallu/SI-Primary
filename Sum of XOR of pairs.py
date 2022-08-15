def sumXOR(arr, n): 
    sum = 0
    for i in range(0, 32):
        zc = 0
        oc = 0
        idsum = 0
        for j in range(0, n):
            if (arr[j] % 2 == 0):
                zc = zc + 1               
            else:
                oc = oc + 1
            arr[j] = int(arr[j] / 2)    
        idsum = oc * zc * (1 << i) 
        sum = sum + idsum;
     
    return 2*sum


t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    print(sumXOR(a,n))
