def knapsack(l, t, p, n):
    K = [[0 for x in range(l + 1)] for x in range(n + 1)]
    x=[0]*n
    for i in range(n + 1):
        for w in range(l + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif t[i-1] <= w:
                K[i][w] = max(p[i-1] + K[i-1][w-t[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    print(K[n][l])
   
j=int(input())
for i in range(j):
    l,n=map(int,input().split())
    t=[]
    p=[]
    for i in range(n):
        a,b=map(int,input().split())
        t.append(a)
        p.append(b)
    knapsack(l,t,p,n)
