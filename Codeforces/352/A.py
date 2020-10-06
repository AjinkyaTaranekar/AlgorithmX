n = int(input())
lst = list(map(int, input().split()))
z = 0
x = 0
for i in range(len(lst)):
    if lst[i] == 0:
        z += 1
    elif lst[i] == 5:
        x += 1
    
if z == 0:
    print(-1)
else:
    if x < 9:
        print(0)
    else:
        for i in range(x/9):
            print(555555555, end="")
        for i in range(z):
            print(0) 