s = input()
b = "hello"
j = k = 0
for i in range(len(s)):
    if s[i] == b[j]:
        j+=1
        k+=1
    if k == 5:
        break;
print("YES" if k == 5 else "NO")