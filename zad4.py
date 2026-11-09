n=int(input("Num:"))

while n<5:
    n=int(input("Num:"))

simple=[]
q=0
p=0

for i in range(1, n+1):
    j=2
    simple=1
    while j<i**0.5:

        if i%j==0:
            simple=0

    if simple:
        simple.append(i)
        q+=1
        
print("All dvojki:\n")
for i in range(q-1):
    if simple[i+1]-simple[i]==2:
        print(simple[i], simple[i+1])
        p=i

print("\nBiggest dvojka:",simple[p],simple[p+1])