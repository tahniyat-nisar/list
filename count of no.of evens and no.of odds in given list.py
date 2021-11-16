elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count1=0
count2=0
while i<len(elements):
    if elements[i]%2==0:
        count1=count1+1
    elif elements[i]%2!=0:
        count2=count2+1
    i=i+1
print("there are",count1,"evens in given list")
print("there are",count2,"odds in given list")
