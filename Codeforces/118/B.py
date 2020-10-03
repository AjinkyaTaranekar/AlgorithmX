n = int(input())
for i in range(-n, n+1):
    top = n - abs(i)
    for j in range(abs(i)):
        print("  ", end="")
    for j in range(top):
        print(j, end=" ")
    for j in range(top, 0, -1):
        print(j, end=" ")
    print(0)
