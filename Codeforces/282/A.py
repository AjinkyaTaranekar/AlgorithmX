x = 0
testCase =int(input())
for i in range(testCase):
    ops = input()
    if ops[0] == '+' or ops[1] == '+':
        x+=1
    else:
        x-=1
print(x)