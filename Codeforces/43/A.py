n = int(input())
lst = []
for i in range(n):
    s = input()
    lst.append(s)
counter = 0
for i in lst:
    curr_fur = lst.count(i)
    if curr_fur > counter:
        counter = curr_fur
        num = i
print(num)
