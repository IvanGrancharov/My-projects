n=int(input("Enter num:"))
smallest=n
totalnums=0
negNums=0
nar=0
last=0

if n==0:
    print("No data.")

while n!=0:
    totalnums+=1
    
    if n>last and last!=0:
        q=n/last
        print("The new num is",q,"times bigger than the last one.")
        nar+=1

    if n<0:
        negNums+=1

    if n<smallest:
        smallest=n

    last=n

    n=int(input("Enter num:"))

print("Number of narastvaniq is", nar)
print("The negative nums are",int((negNums/totalnums)*100),"percent of all nums")
print("The smallets num is", smallest)