from collections import Counter
from collections import OrderedDict 

def factorial(n): 
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);

testcases=int(input())
for testcase in range(testcases):
    
    n, k = [int(x) for x in input().strip().split()]
    mainSequence = [int(x) for x in input().strip().split()]
    interestingSubSequence = 0
    mainSequence.sort()
    
    count=dict(Counter(mainSequence)) 
    sum=0
    for i in count:
        sum+=count[i]
        if(sum>=k):
            break
    interestingSubSequence=mainSequence[:sum]
    
    count=dict(Counter(interestingSubSequence))
    count=OrderedDict(count)
        
    print(int(factorial(list(count.values())[len(count)-1])/(factorial(sum-k)*factorial(k-sum+list(count.values())[len(count)-1]))))
