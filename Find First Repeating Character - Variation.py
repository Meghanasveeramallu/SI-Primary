def f(s):
    a=set()
    for i in range(len(s)):
        if s[i] in a:
            return s[i]
        else:
            a.add(s[i])
    return '.'

t=int(input())
for i in range(t):
    s=input()
    print(f(s))
