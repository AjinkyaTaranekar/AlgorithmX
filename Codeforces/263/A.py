x,y =0,0
for i in range(1,6):
    row = list(map(int,input().split()))
    if row.count(1)==1:
        y = row.index(1)+1
        x = i
print(abs(x-3)+abs(y-3))