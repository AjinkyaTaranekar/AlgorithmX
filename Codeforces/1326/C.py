mod=998244353
n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
maxi = []

for i in range(n):
    if(a[i]<=n and a[i]>n-k):
        maxi.append(i)

sum=0
num=1
for i in range(k):
    sum+=(n-i)
for i in range(1,k):
	num*=(maxi[i]-maxi[i-1])
	num%=mod

print(sum,num)