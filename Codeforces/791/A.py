a,b = map(int,input().split())
i = 0
while True:
    i+=1
    if a*3**i > b*2**i:
       break
print(i)