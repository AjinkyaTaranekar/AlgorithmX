s = input()
i = s.find("AB")
j = s.rfind("BA")
i2 = s.rfind("AB")
j2 = s.find("BA")
print("YES" if i!=-1 and j!=-1 and (abs(i-j)>1 or abs(i2-j2)>1) else "NO")