a=[2, 4, 6, 8]
i=0
c=[]
while i<len(a)-1:
    b=(a[i+1]-a[i])
    c.append(b)
    i=i+1
print(c)

Output:[2,2,2]
