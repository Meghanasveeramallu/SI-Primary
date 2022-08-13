import collections 
def frequencySort(nums):
    count = collections.defaultdict(int)
    for num in nums:
        count[num] += 1

    list_keys = count.keys()
    occurrance = collections.defaultdict(list)
    for ky in list_keys:
        occurrance[count[ky]].append(ky)

    list_occur = list(sorted(occurrance.keys()))
    result = []
    for ele in list_occur:
        occurrance[ele].sort()
        for y in occurrance[ele]:
            result += [y]*ele
    for i in result:
        print(i,end=' ')
    print()
    #return result

t=int(input())
for i in range(t):
    n=int(input())
    a=[int(s) for s in input().split()]
    frequencySort(a)
