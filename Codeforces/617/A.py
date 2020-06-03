n = int(input())
count=0
while n-5 >= 0:
    n-=5
    count+=1
while n-4 >= 0:
    n-=4
    count+=1
while n-3 >= 0:
    n-=3
    count+=1
while n-2 >= 0:
    n-=2
    count+=1
while n-1 >= 0:
    n-=1
    count+=1
print(count)