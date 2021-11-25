a=[78,34,15,61,12,89]
i=0
min=a[i]
while i<len(a):
     if a[i]<min:
         min=a[i]
     i=i+1
print(min)


j=0
sec_min=a[j]
while j<len(a):
    if a[j]<sec_min:
        if a[j]!=min:
            sec_min=a[j]
    j=j+1
print(sec_min)
