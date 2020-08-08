n = int(input())
s = [i for i in input()]
res=0
i = 1
while(i<len(s)):
    if s[i-1]==s[i]:
        s.remove(s[i])
        res+=1
    else:
        i+=1
print(res)