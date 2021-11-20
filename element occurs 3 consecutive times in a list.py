a=[1, 1, 1, 64,64,64, 23, 64, 22, 22, 22]
i=0
while i<len(a)-2:
    if a[i]==a[i+1]==a[i+2]:
        print(a[i])
    i=i+1
    
#    Output:1
#           64
#           22
