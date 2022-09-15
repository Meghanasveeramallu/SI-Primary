t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=[int(s) for s in input().split()]
    k=k%n
    for i in range(n):
        print(a[(i-k+n)%n],end=' ')
    print()
