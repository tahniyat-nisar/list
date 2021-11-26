a=[1,2,3,4,5,6]
i=0
sum1=0
sum2=0
while i<len(a):
    if i%2==0:
        sum1=sum1+a[i]
    elif i%2!=0:
        sum2=sum2+a[i]
    i=i+1
print(sum1)
print(sum2)
