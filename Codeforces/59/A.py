n = input()
u,l=0,0
for i in n:
    if i.isupper():
        u+=1
    else:
        l+=1
print(n.lower() if l>=u else n.upper())