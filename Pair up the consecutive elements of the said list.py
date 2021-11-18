a=[1, 2, 3, 4, 5, 6]
i=0
c=[]
while i<len(a)-1:
    b=[a[i],a[i+1]]
    c.append(b)
    i=i+1
print(c)
    
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
