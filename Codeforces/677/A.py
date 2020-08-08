n,h = map(int,input().split())
a = list(map(int,input().split()))
res = 0
for i in range(n):
    if a[i] > h:
        res+=1
    res+=1
print(res)