k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input()) + 1
print(len(set([i for i in range(k,d,k)]+[i for i in range(l,d,l)]+[i for i in range(m,d,m)]+[i for i in range(n,d,n)])))