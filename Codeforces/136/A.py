n = int(input())
p = list(map(int,input().split()))
m = {v:i+1 for i,v in enumerate(p)}
print(' '.join([str(m[i+1]) for i in range(n)]))