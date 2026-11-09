N=int(input("Number: "))
dByThree=0
posSum=0
posNums=0

if N<=0:
    print("Invalid number")
else:
    i=0

    for i in range(0,N):
        n=int(input("Enter num:"))

        if n%3==0:
            dByThree+=1

        if n>0:
            posSum+=n
            posNums+=1

    print("The number of nums divided by 3 is",dByThree)

    if posSum==0:
        print("No positive nums.")

    else:
        posAvg=posSum/posNums
        print("The avg of positive nums is",posAvg) #ne e zakrygleno




