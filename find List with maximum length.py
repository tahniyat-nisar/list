a=[[0], [1,2,8,0,7,6, 3], [5, 7,1,2,3], [9, 11], [13, 15, 17]]
i=0
max=0
while i<len(a):
    b=(len(a[i]))
    if b>max:
        max=b
        c=a[i]
    i=i+1
print(max,c)

output:(7,[1,2,8,0,7,6,3])
