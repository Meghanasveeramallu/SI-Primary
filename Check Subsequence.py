def f(a,b):
    i=0 
    j=0    
    while i<len(a) and j<len(b):
        if a[i]==b[j]:
            i+=1
        j+=1
        
    if i==len(a):
        return "Yes"
    return "No"


t=int(input())
for i in range(t):
    a,b=map(str,input().split())
    print(f(a,b))
