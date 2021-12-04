user_input=(input("enter a binary number:"))
BN=list(user_input)
index=-1
length=len(BN)
count=0
sum=0
while index<count and count<length:
    element=(int(BN[index])*(2**(count)))
    sum=sum+element
    index=index-1
    count=count+1
print(sum)


# binary=int(input("enter a binary number:"))
# B=str(binary)
# c=list(B)
# length=len(c)
# i=length-1
# count=0
# sum=0
# while i>=0 and count<=length:
#       cal=int(c[i])*(2**count)
#       sum=sum+cal      
#       count+=1
#       i-=1
# print(sum)
# print(cal)
