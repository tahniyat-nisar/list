a=[1,3,[4,6,7],7,8,9,[6],10]
sum1=0
i=0
sum2=0
while i<len(a):
    k=(a[i])
    if type(k)==list:
        j=0
        while j<len(k):
            sum1=sum1+k[j]
            j=j+1
    elif type(k)==int:
        m=k
        sum2=sum2+m
    i=i+1
print(sum1+sum2)
