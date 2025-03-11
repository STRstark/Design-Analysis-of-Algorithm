n = int(input())
for _ in range(n):
    a , k = map(int , input().split(" "))
    sum = 0
    cur = 1
    mul = a+1
    while(a >= k):
        if a and 1 :
            sum +=cur
        a>>=1
        cur <<= 1
    print(mul * sum /2)