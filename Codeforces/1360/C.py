testcase = int(input())
for test in range(testcase):
    n = int(input())
    num = list(map(int,input().split()))
    even = []
    odd = []
    dict = {i:0 for i in range(max(num)+2)}
    for i in num:
        if i % 2 == 0:
            even.append(i)
            dict[i]+=1
        else:
            odd.append(i)

    e = len(even)
    o = n - e

    if e%2==0 and o%2==0:
        print("YES")
        
    elif e%2!=o%2:
        print("NO")
    else:
        flag = False
        for i in range(o):
            x = odd[i]
            if dict[x+1]!=0 or dict[x-1]!=0:
                flag = True
                break
        print("YES" if flag else "NO")