n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
c=[]
while i<len(n):
    j=0
    count=0
    while j<len(n):
            if n[i]==n[j]:
                count=count+1
                if count>=2:
                    if n[i] not in c:
                        c.append(n[i])
            j=j+1
    i=i+1
print(c)

# Output:[19,17,12]












# extract all elements whose frequency is greater than K.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output: [4, 3]

n = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8] 
i=0
c=[]
while i<len(n):
    j=0
    count=0
    while j<len(n):
            if n[i]==n[j]:
                count=count+1
                if count>3:
                    if n[i] not in c:
                        c.append(n[i])                    
            j=j+1  
    i=i+1
print(c)
