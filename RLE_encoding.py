a="aaabccdddd"
final=""

i=0

while i<len(a):
    count=1

    while i+1<len(a) and a[i]==a[i+1]:
        count+=1
        i+=1

    final=final+a[i]+str(count)

    i+=1

print(final)