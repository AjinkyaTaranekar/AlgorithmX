n,m,a = list(map(int,input().split()))
if m%a==0:
    r1=m//a
else:
    r1=m//a+1
 
if n%a==0:
    r2=n//a
else:
    r2=n//a+1
 
print(r1*r2)