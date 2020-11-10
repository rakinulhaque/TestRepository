num=int(input())
list=[]
while num>0:
    digit=num%10
    if digit not in list:
        list.append(digit)
    num=num//10
print(len(list))