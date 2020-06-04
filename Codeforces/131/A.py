s = input()
flag = True
for i in range(1,len(s)):
    if s[i].islower():
        flag = False

if flag:
    for i in s:
        if i.islower():
            print(i.upper(),end='')
        else:
            print(i.lower(),end='')
else:
    print(s)