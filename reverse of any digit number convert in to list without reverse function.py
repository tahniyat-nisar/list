n=int(input("enter a number:"))
a=list(str(n))
c=[]
i=0
while i<len(a):
    b=int(a[i])
    c.append(b)
    i=i+1
j=0
length=len(c)
d=[]
while j<len(c):
    j=j+1
    print(c[-j])
    d.append(c[-j])
    print(d)
    
   Input:1234
    Output1:[1,2,3,4]
    Output2:  4
              3
              2
              1
    Output3:[4,3,2,1]
