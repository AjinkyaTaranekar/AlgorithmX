testcase = int(input())
for test in range(testcase):
    n = int(input())
    mat = []
    for i in range(n):
        row = list(input())
        row = [ int(i) for i in row]
        mat.append(row)
    
    flag = False
    for i in range(n-1):
        for j in range(n-1):
            if mat[i][j]==1:
                if mat[i+1][j]==0 and mat[i][j+1]==0:
                    flag = True 
                    break
    print("YES" if not flag else "NO")