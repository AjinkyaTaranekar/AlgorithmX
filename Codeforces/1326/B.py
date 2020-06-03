n = int(input())
a = list(map(int,input().split()))
b = [-1000]*n

b[0]=a[0];
print(b[0],end = " ")

m=b[0]

for i in range(1,n):
    b[i]=a[i]+m
    m=max(m,b[i])
    print(b[i],end = " ")
