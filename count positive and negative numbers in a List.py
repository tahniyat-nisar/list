a= [2, -7, 5, -64, -14]
i=0
count1=0
count2=0
while i<len(a) and count1<len(a) and count2<len(a):
    if a[i]>0:
        count1=count1+1
    elif a[i]<0:
        count2=count2+1
    i=i+1
print("No.of positives in given list",count1)
print("No.of negatives in given list",count2)

# Output: pos = 2, neg = 3
