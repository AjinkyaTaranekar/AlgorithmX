n = int(input())
res = 0
for i in range(n):
    a,b = map(int,input().split())
    if b - a >1:
        res+=1
print(res)