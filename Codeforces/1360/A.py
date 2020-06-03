testcase = int(input())
for test in range(testcase):
    a,b = map(int,input().split())
    print(int(max(min(a,b)*2,max(a,b))**2))