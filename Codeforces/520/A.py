n = int(input())
s = input().lower()
if n < 26:
    print("NO")
else:
    alpha = {chr(i+97):False for i in range(26)}
    for i in s:
        alpha[i] = True
    print("YES" if sum(alpha.values()) == 26 else "NO" )