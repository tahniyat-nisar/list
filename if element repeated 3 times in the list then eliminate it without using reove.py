n= [1, 1, 2, 3, 4, 1, 5, 1, 2,2]
i=0
c=[]
d=[]
while i<len(n):
    j=0
    count=0
    while j<len(n):
            if n[i]==n[j]:
                count=count+1
                if count>=3:
                    if n[i] not in c:
                        c.append(n[i])
            j=j+1
    i=i+1
k=0
while k<len(n):
    if n[k] in c:
        pass
    else:
        d.append(n[k])
    k=k+1   
print(d)

# output:[3,4,5]
