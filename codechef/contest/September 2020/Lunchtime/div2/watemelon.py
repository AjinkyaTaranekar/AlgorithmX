test = int(input())
for t in range(test):
	n = int(input())
	l = list(map(int, input().split()))
	if sum(l) == 0:
		print("YES")
	elif sum(l)<0:
		print("NO")
	else:
		print("YES")