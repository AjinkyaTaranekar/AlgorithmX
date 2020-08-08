n = int(input())
res = 0
c = 0
for i in range(n):
    a,b = map(int,input().split())
    c-=a
    c+=b
    res = max(res,c)
print(res)