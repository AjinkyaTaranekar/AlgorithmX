testcase = int(input())
for test in range(testcase):
    n = int(input())
    ath = list(map(int,input().split()))
    ath.sort()
    diff = 10**18
    for i in range(n-1):
        diff = min(diff , ath[i+1] - ath[i])
    print(diff)