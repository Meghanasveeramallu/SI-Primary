n=int(input())
for i in range(n):
    a=[int(s) for s in input().split()]
    b=[int(s) for s in input().split()]
    ar1=abs(a[0]-a[2])*abs(a[1]-a[3])
    ar2=abs(b[0]-b[2])*abs(b[1]-b[3])
    x_dist=min(a[2],b[2])-max(a[0],b[0])
    y_dist=min(a[3],b[3])-max(a[1],b[1])
    ar3=0
    if x_dist>0 and y_dist>0:
        ar3=x_dist*y_dist
    print(ar1+ar2-ar3)
