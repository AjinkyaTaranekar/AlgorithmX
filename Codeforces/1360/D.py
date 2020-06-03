testcase = int(input())
for test in range(testcase):
    n,k = map(int,input().split())
    if k >= n:
        print(1)
    else:
        ans = 10**9+7
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                if i<=k and n/i>k:
                    ans=min(ans,n//i)
                elif n/i<=k and i>k:
                    ans=min(ans,i)
                elif n/i<=k and i<=k:
                    ans = min(ans,min(i,n//i))
        print(ans)