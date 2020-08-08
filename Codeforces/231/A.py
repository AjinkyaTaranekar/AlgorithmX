n = int(input())
res = 0
for i in range(n):
    if sum(list(map(int,input().split()))) > 1:
        res+=1
print(res)