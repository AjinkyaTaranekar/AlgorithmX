t=int(input())
while t>0:
    t-=1
    n,m=map(int,input().split())
    k=0
    
    while n>0:
        a,b=map(int,input().split())
        c,d=map(int,input().split())
        if  b==c:
            k=1
        n-=1
    if k==0:
        print("NO")
    else:
        if m%2==0:
            print("YES")
        else:
            print("NO")