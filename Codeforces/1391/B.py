testcase = int(input())
for test in range(testcase):
    n,m = map(int,input().split())
    grid = []
    for i in range(n):
        grid.append([i for i in input()])
    count = 0
    for i in range(m-1):
        count += (grid[n-1][i] != 'R')
      
    for i in range(n-1):
        count += (grid[i][m - 1] != 'D')
    print(count)
    
