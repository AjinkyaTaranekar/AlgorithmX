def solve():
    n = int(input())
    lst = list(map(int, input().split()))
    lst2 = []
    st = set()
    dictt = {}
    ktt = set(lst)
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            cnt = 0
            if lst[i] == lst[j]:
                if not lst[i] in st:
                    lst2.append(j-i)
                    dictt[lst[i]] = j-i
                    st.add(lst[i])
                    break
                else:
                    if j - i == dictt[lst[i]]:
                        continue
                    else:
                        temp = j
                        while temp:
                            temp -= dictt[lst[i]]
                            if temp == dictt[lst[i]]:
                                break
                            elif temp < dictt[lst[i]]:
                                print(0)
                                return 
                cnt += 1
    j = 0
    print(len(ktt))
    stt = sorted(ktt)
    for i in stt:
        if not i in st:
            print(i, 0)
        else:
            print(i, lst2[j])
            j += 1


if __name__== '__main__':
    solve()
