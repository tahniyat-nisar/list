# Convert the said list of strings into list of lists:

a=['Red', 'Maroon', 'Yellow', 'Olive']
i=0
j=[]
while i<len(a):
    b=(list(a[i]))
    j.append(b)
    i=i+1
print(j)

# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]

