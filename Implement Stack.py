def pop(a):
    if len(a)==0:
        print("Empty")
    else:
        print(a.pop(len(a)-1))

t=int(input())
a=[]
for i in range(t):
    s=input().split()
    if s[0]=="push":
        a.append(int(s[1]))
    else:
        pop(a)
