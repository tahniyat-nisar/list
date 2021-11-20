# if we give 9119 the function should return 811181, as the square of 9 is 81 and square
# of 1 is 1.
n=int(input("enter a number:"))
z=list(str(n))
i=0
c=[]
while i<len(z):
    b=int(z[i])**2
    c.append(b)
    print(c[i],end="")
    if i==len(z)-1:
        print(end= " ")
    i=i+1
