a="a12b2C4"
final=""
i=0

while i<len(a):
    count=""
    j=1
    final=final+a[i]
    count=count+a[i+1]
    letter=i
    i+=1

    while i+1<len(a) and a[i+1]>='0' and a[i+1]<='9':
        count=count+a[i+1]
        i+=1

    while j<int(count):
        final=final+a[letter]
        j+=1

    i+=1

print(final)