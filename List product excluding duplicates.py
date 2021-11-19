# List product excluding duplicates.
s = [6,1,3,5,6,3,1]
i=0
c=[]
p=1
while i<len(s):
    j=0
    count=0
    while j<len(s):
        if s[i]!=s[j]:
            count=count+1
            if count<=2:
                if s[i] not in c:
                    c.append(s[i])
                    p=p*s[i]
        j=j+1        
    i=i+1
print(p)
# Output: 90
