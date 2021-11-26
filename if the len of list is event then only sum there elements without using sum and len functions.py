a=[1,2,3,4,5]
count=0
i=0
while i<len(a):
    count=count+1
    i=i+1
print(count)
if count%2==0:
        j=0
        sum=0
        while j<len(a):
            sum=sum+a[j]
            j=j+1
            print(sum)
else:
        print("not divisible")
