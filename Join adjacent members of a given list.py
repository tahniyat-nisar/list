a=['1', '2', '3', '4', '5', '6', '7', '8']
i=0
j=1
c=[]
while i<len(a) and j<len(a):
    k=a[i]+a[j]
    c.append(k)
    i=i+1
    j=j+1
print(c)
# # Join adjacent members of a given list:
# # ['12', '23' , '34', '45' , '56', '67' , '78']




a=['1', '2', '3', '4', '5', '6', '7', '8']
i=0
j=1
c=[]
while i<len(a) and j<len(a):
    k=a[i]+a[j]
    c.append(k)
    i=i+2
    j=j+2
print(c)
# Join adjacent members of a given list:
# ['12', '34', '56', '78']
