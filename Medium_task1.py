limit = int(input())
num1, num2 = 0, 1

if limit == 1:
   print(num1)
else:
    while num1 <= limit:
       print(num1)
       n3 = num1 + num2
       num1 = num2
       num2 = n3