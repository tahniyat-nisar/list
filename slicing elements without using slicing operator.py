List =['a', 1, 2, 5, 'b', 'q']
n=int(input("enter a number:"))
a=-(n-len(List))
i=-((len(List)-a))
while i<=-1:
    print(List[i])
    i+=1
# Input:3
# output:5
#        b
#        q


List =['a', 1, 2, 5, 'b', 'q']
n=int(input("enter a number:"))
i=-1
while i>=-n:
print(List[i])
i-=1
#Input:2
# output:q
#        b
