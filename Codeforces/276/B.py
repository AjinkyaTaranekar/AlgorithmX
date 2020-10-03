from collections import Counter
s = input()
s = list(s)
cnt = 0
dictt = Counter(s)
print(dictt)
if s[::-1] == s:
    print("First")
else:
    for i in range(len(s)):
        ccnt = s.count(s[i])
        if ccnt % 2 != 0:
            temp = s[::]
            temp.remove(s[i])
            cnt += 1
