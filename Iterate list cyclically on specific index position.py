r=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
n=int(input("enter a number:"))
i=n
c=[]
while i<len(r):
    (c.append(r[i]))
    i=i+1
j=0
d=[]
while j<n:
    d.append(r[j])
    j=j+1
print(c+d)

# Sample output:
#   Iterate list cyclically on specific index position 3 :
# ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
