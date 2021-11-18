a=[5, 6, [], 3, [], [], 9]
i=0
c=[]
while i<len(a):
    if a[i]==[]:
        pass
    else:
        c.append(a[i])
    i=i+1
print(c)

# List after empty list removal: [5, 6, 3, 9]
