k,r = map(int,input().split())
ans = 0
sum = 0
while True:
    ans+=1
    sum = ans*k
    if sum % 10 == 0:
        break
    if (sum - r) % 10 == 0:
        break
print(ans)