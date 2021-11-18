a=[12, 67, 98, 34]
i=0
k=[]
while i<len(a):
    b=a[i]%10
    c=a[i]//10
    d=b+c
    k.append(d) 
    i=i+1
print(k)
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
