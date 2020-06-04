s = input()
ans = 0
prev = 'a'
for i in s:
    ans+=min(abs(ord(i) - ord(prev)), 26 - abs(ord(i) - ord(prev)))
    prev = i
print(ans)