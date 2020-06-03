s = input()
l = len(set([i for i in s]))
if l % 2:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")