exp = list(map(int,input().split("+")))
exp.sort()
print("+".join([str(i) for i in exp]))