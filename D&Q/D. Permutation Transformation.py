ans=[]
per = []
def calc(permit, depth):
    if not permit:
        return
    M = permit.index(max(permit))  
    N = per.index(max(permit))
    ans[N] = depth  
    
    calc(permit[:M], depth + 1)         
    calc(permit[M+1:], depth + 1)  

n = int(input())
for i in range(n):
    L = int(input())
    per = list(map(int , input().split(" ")))
    ans=[0]*L
    calc(per , 0)
    print(*ans)