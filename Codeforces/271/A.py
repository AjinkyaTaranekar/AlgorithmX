n = int(input())
while(True):
    n+=1
    if len(list(str(n)))==len(set(str(n))):
        break
print(n)