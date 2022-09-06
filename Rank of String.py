M=256
count=[0]*(M + 1)

def fact(n):
    return 1 if(n <= 1) else (n * fact(n - 1))

def f(s):
    for i in range(len(s)):
        count[ord(s[i])]+=1
    for i in range(1,M):
        count[i] += count[i - 1]

def updatecount(ch):
    for i in range(ord(ch),M):
        count[i]-=1

def findRank(s):
    len1 = len(s)
    mul = fact(len1)
    rank = 1
    f(s)
    for i in range(len1):
        mul = mul//(len1 - i)
        rank += count[ord(s[i]) - 1] * mul;
        updatecount(s[i])
    return rank

t=int(input())
for i in range(t):
    s = input()
    print(findRank(s))
