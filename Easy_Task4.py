num=int(input())
count=0
for i in range(2,(num//2)+1,1):
    if(num%i==0):
        count+=1
        if(count>=1):
            break
if(count==0):
    print("Prime")