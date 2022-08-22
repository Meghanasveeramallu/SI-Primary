def largestNumber(nums):
    nums=list(map(str,nums))
    nums.sort()
    nums=nums[::-1]
    res=[str(nums[0])]
    for n in nums[1:]:                
        if res[-1]+str(n)<str(n)+res[-1]:
            j=len(res)-1
            while j>0 and str(n)+res[j-1]>res[j-1]+str(n):
                j-=1

            res.insert(j,str(n))
        else:
            res.append(str(n))
    ans="".join(res)
    return int(ans)

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    print(largestNumber(a))
