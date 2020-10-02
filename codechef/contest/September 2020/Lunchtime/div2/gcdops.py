import math
def isPrime(a):
	if a==1 or a==2:
		return True
	for i in range(2,int(math.sqrt(a))+1):
		if a%i==0:
			return False
	return True	
def gcd(a,b):
	if b==0:
		return a
	gcd(b, a%b)
test = int(input())
for t in range(test):
	n = int(input())
	l = list(map(int, input().split()))
	flag = True
	for i in range(1,n+1):
		if i!=l[i-1]:
			if i%l[i-1]!=0:
				flag = False
	if flag:
		print("YES")
	else:
		print("NO")