n=int(input())
for i in range(n):
    m=[int(s) for s in input().split()]
    A=[]
    for i in range(m[0]):
        A.append([int(s) for s in input().split()])
    n=[int(s) for s in input().split()]
    B=[]
    for i in range(n[0]):
        B.append([int(s) for s in input().split()])
    result=[[0 for i in range(n[1])] for j in range(m[0])]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    for i in range(len(result)):
        for j in range(len(result[0])):
            print(result[i][j],end=' ')
        print()
