import math
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    print(int(math.ceil(n/k))*k-n if n > k else k-n )