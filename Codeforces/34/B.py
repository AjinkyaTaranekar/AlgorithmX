n, m = input().split()
n, m = int(n), int(m)
lst = list(map(int, input().split()))
lst = sorted(lst)
cnt = 0
cntm = 0
for i in range(len(lst)):
    if lst[i] < 0 and cntm < m:
        cnt += lst[i]
        cntm += 1
    else:
        break

print(abs(cnt))