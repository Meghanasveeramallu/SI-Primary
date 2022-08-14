n=int(input())
for i in range(n):
    p=int(input())
    count = 0
    while(p >= 5):
        p //= 5
        count += p
    print(count)
