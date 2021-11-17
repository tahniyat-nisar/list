# Remove the last 3 elements from the said list:
n=int(input("Enter how many no.of elements you want to eliminate from last")
a=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
i=0
length=len(a)-n
c=[]
while i<length:
    w=(a[i])
    c.append(w)
    i=i+1
print(c)
