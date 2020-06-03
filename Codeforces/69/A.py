n = int(input())
xsum,ysum,zsum=0,0,0
for i in range(n):
    x,y,z = map(int,input().split())
    xsum+=x
    ysum+=y
    zsum+=z
if xsum==0 and ysum==0 and zsum==0:
    print("YES")
else:
    print("NO")