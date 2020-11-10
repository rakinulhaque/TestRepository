num = int(input())     
while(num > 0):    
    remainder = num %10    
    num = num //10 
    print(remainder,end="")