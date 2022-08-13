f=[1]*(1000001)
#print(f)
k=(10**9)+7
for i in range(2,1000001):
    #print(i)
    f[i]=(f[i-1]*i)%k

t=int(input())
for i in range(t):
    n=int(input())
    print(f[n])
