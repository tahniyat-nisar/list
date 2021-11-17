# Dimension of the said matrix:
a=[[0, 1, 2], [2, 4, 5]] #(2(main list len),3(sub list len))
i=0
count1=0
while i<len(a) and count1<=len(a):
    count1=count1+1
    j=0
    count2=0
    while j<len(a[i]):
        count2=count2+1
        j=j+1
    i=i+1
c=(count1,count2)
c=tuple(c)
print(c)
