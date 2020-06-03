n,k = list(map(int,input().split()))
L = list(map(int,input().split()))
print (sum([L[i]>=L[k-1] and L[i]>0 for i in range(n)]))