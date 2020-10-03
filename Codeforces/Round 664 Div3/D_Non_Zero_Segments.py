n = int(input())
a = list(map(int,input().split()))

prefixes = set()
curr = 0
ans = 0
for i in range(n):
	curr += a[i]
	if curr==0 or curr in prefixes:
		ans += 1
		curr = a[i]
		prefixes.clear()
	prefixes.add(curr)

print(ans)