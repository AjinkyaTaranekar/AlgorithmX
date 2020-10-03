t=int(input())
while t>0:
    t-=1
    n=int(input())
    s=[n-1]
    for i in range(2,n+1):
        a=i-1
        if n%i==0:
            a+=n//i-1
        else:
            a+=n//i
        s.append(a)
        if s[-1]>s[-2]:
            break
    print(min(s))        