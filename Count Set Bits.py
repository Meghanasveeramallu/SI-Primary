def countSetBits(n):
    count = 0
    while (n):
        n &= (n-1)
        count+= 1
     
    return count
 
t=int(input())
for i in range(t):
    n=int(input())
    print(countSetBits(n))
