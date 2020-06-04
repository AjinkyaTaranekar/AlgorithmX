n = int(input())
s = input()
ans = 0
while s.count("xxx") !=0:
    ans+=1
    s = s.replace("xxx","xx",1)
print(ans)