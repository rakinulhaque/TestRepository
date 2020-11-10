row=int(input())
for i in range(1,row+1,1):
    for j in range(1,row-i+1,1):
        print(" ",end="")
    for j in range(1,2*i,1):
        if(i==row or j==2*i-1 or j==1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,row,1):
    for j in range(1,i+1,1):
        print(" ",end="")
    for j in range(1,2*(row-i),1):
        if(j==1 or j==2*(row-i)-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()