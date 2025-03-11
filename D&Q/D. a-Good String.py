def calc(s , c):
    if len(s) == 1:
        return int(s[0] != c)
    
    mid = len(s) // 2
    cntl = calc(s[:mid], chr(ord(c) + 1))
    cntl += mid - s[mid:].count(c)
    
    cntr = calc(s[mid:], chr(ord(c) + 1))
    cntr += mid - s[:mid].count(c)
    
    return min(cntl, cntr)    

x = int(input())
for _ in range(x):
    x = int(input())
    S = input()
    print(calc(S , 'a'))

