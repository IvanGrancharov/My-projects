a=int(input("Enter a:"))
b=int(input("Enter b:"))

if a>b:
    q=a
    a=b
    b=q

suv=[]
iz=0

for i in range(a,b+1):
    sum=0
    for j in range (1,i):
        if i%j==0:
            sum+=j

    if sum==i:
        suv.append(i)

    elif sum>i:
        iz+=1

print("The suvur6eni nums are",suv)
print("The number of izobilni nums is",iz)