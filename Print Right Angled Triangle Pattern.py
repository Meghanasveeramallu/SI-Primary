a=int(input())
for i in range(a):
    print("Case #{}:".format(i+1))
    b=int(input())
    for i in range(1,b+1):
        c=b-i
        for j in range(c):
            print(' ',end="")

        for j in range(i):
            print('*',end="")
        print()
