s = [6,1,3,5,6,3,1]
i=0
c=[]
while i<len(s):
    j=0
    count=0
    while j<len(s):
        if s[i]!=s[j]:
            count=count+1
            if count<=2:
                if s[i] not in c:
                    c.append(s[i])
        j=j+1        
    i=i+1
print(c)

[6,1,3,5}
