def add(s):
        dictt={}
	for i in s:
		for j in i:
			try:
				dictt[j]+=1
			except KeyError:
				dictt[j]=1
	return dictt

def main():
	first = add(input().split())
	for i in input().split():
		for j in i:
			if j not in first or first[j]==0:
				print ('NO')
				exit()
			else:
				first[j]-=1
	print ('YES')

if __name__== '__main__':
	main()