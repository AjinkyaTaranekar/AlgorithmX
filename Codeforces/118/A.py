s = input().lower()
res = ""
for i in s:
    if i not in 'aeiouy':
        res+='.'+i
print(res)