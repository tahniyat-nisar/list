12 # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304 # Should return '70000 + 300 + 4'
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
    # print(c[-j])
    d.append(c[-j])
print(d)
p=1
k=0
while k<len(d):
    e=d[k]
    # print(e)
    p=(p*10)
    r=p//10
    print(r*e,end="+")
    k=k+1
print()
    

