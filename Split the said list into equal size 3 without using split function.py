a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
i=0
b=[]
while i<len(a):
    j=i
    c=[]
    while j<3+i:
        c.append(a[j])
        j+=1
    b.append(c)
    i=i+3
print(b)


# [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
