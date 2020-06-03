n = input()
count = 0
for i in n:
    if i in ["4","7"]:
        count+=1        
if count == 4 or count == 7:
    print("YES")
else:
    print("NO")
        