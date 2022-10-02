f=[[0 for i in range(2002)] for j in range(2002)]
k=(10**9)+7
for i in range(2002):
    f[i][0]=1
for i in range(1,2002):
    for j in range(1,2002):
        f[i][j]=(f[i-1][j-1]+f[i-1][j])%k
        
t=int(input())
for i in range(t):
    n,r=map(int,input().split())
    print(f[n][r])
