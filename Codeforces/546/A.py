k,n,w = map(int,input().split())
sum = w*(w+1)*k//2
loan = sum - n
if loan < 0:
    loan = 0
print(loan)