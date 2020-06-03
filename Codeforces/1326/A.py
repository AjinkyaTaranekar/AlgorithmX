testCase = int(input())
for i in range(testCase):
    n = int(input())
    if n == 1:
        print(-1)
    else:
        print(2,end="")
        for j in range(1,n):
            print(3,end="")
        print()