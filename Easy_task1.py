count=1
for num in range(1,31,1):
    if(num%3==0 or num%5==0):
        print(num)
        count+=1
print("Amount:",count)