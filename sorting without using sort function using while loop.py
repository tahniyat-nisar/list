a=[1,2,5,3,4,6]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j=j+1
    i=i+1
print(a)

# Output:[1,2,3,4,5,6] #in ascending order




a=[1,2,5,3,4,6]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]>[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j=j+1
    i=i+1
print(a)

# Output:[6,5,4,3,2,1] #in descending order

