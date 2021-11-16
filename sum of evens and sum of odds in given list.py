elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
# count1=0
# count2=0
sum1=0
sum2=0
while i<len(elements):
    if elements[i]%2==0:
        # count1=count1+1
        sum1=sum1+elements[i]
    elif elements[i]%2!=0:
        # count2=count2+1
        sum2=sum2+elements[i]
    i=i+1
# print("there are",count1,"evens in given list")
# print("there are",count2,"odds in given list")
print("The sum of evens in a given list",sum1)
print("The sum of odds in a given list",sum2)
