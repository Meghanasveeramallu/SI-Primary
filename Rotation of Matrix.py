def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp

def printMatrix(A):
    N = len(A[0])
    for i in range(N):
        for j in range(N):
            print(A[i][j],end=" ")
        print()

t=int(input())
for k in range(t):
    n=int(input())
    A=[]
    for p in range(n):
        row=[int(s) for s in input().split()]
        A.append(row)
    rotate90Clockwise(A)
    print("Test Case #{}:".format(k+1))
    printMatrix(A)
