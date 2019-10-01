def lessthan(n):
    i=1
    while(1):
        if(n<pow(2,i)):
            return i-1
        i+=1
        
tc=int(input())
for i in range(tc):
    n=int(input())
    if(n==1):
        print("0")
    
    elif(n==2 or n==3):
        print("1")
        
    else:
        res=lessthan(n)
        if(res%4==2):
            print("2")
    
        elif(res%4==3):
            print("3")
    
        elif(res%4==0):
            print("0")
            
        elif(res%4==1):
            print("9")