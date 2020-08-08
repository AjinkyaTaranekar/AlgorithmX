import math
n = int(input())
for i in range(n):
    num = int(input())
    if num&1:
        num-=1
    print(math.gcd(num,num//2))