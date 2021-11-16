a=str(input("Enter a Number:"))
a=list(a)
b=0
while b<len(a):
    a[b]=int(a[b])# if you add (**2) you will get squares
    b+=1
print(a)
i=0
while i<len(a):
    print(a[i],end='')
    i=i+1