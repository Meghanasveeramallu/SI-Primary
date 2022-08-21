import math
def f(a,b):
    return (math.floor(math.sqrt(b))-math.ceil(math.sqrt(a))+1)

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    print(f(a,b))
