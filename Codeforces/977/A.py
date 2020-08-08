n,k = map(int,input().split())
for i in range(k):
    n = str(n)
    if n[-1]!='0':
        n = int(n)-1
    else:
        n = int(n)//10
print(n)