

t=int(input())
while t>0:
    t-=1
    n,x=map(int,input().split())
    if n==1 or n==2:
        print(1)
    else:
        if (n-2)%x==0:
            print((n-2)//x+1)
        else:
            print((n-2)//x+2)