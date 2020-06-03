MAX=10**6
prime=[True]*(MAX+1)
prime[0]=prime[1]=False
for i in range(2,int(MAX**0.5)):
    if prime[i]==True:
        for j in range(i*i,len(prime),i):
            prime[j]=False
 
n = int(input())
nums = list(map(int,input().split()))
for i in nums:
    x=i**0.5
    if x.is_integer():
        if prime[int(x)]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")    