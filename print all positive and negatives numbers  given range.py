# Input: start = -4, end = 5
# Output: -4, -3, -2, -1
a=range(-4,5)
i=4
while i in a:
    print(-i,end=", ")
    if -i==-1:
        break
    i=i-1


# Input: start = -4, end = 5
# Output: 0, 1, 2, 3, 4, 5
a=range(-4,5)
i=0
while i in a:
    print(i,end=", ")
    i=i+1




a=range(-4,5)
i=4
while i<len(a):
    print(a[i],end=", ")
    if a[i]==4:
        c=a[i]+1
        print(c)
    i=i+1
# Input: start = -4, end = 5
# Output: 0, 1, 2, 3, 4, 5
