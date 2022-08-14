a=int(input())
for i in range(a):
    h=int(input())
    print("Case #{}:".format(i+1))
    b=int((h+1)/2)
    for i in range(1, b+1):
        for j in range(1,b-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    for i in range(b-1,0, -1):
        for j in range(1,b-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
