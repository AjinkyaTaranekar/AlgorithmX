import math
n = int(input())
lst = list(map(int, input().split()))
mn = math.inf
for i in range(1, len(lst)):
    if abs(lst[i]-lst[i-1] < mn):
        mn = abs(lst[i] - lst[i-1])
        ans = (i, i +1)

if abs(lst[-1] - lst[0]) < mn:
    ans = (1, n)
if abs(lst[-1] - lst[0]) == mn:
    ans = (n, 1)
    
print(ans[0], ans[1])