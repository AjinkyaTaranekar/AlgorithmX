n,m = map(int,input().split())
days = 0
while n !=0:
    n-=1
    days +=1
    if days % m == 0:
        n+=1
    
print(days)