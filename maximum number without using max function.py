numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
length_number=len(numbers)
maximum=0
index=0
while index<len(numbers):
    element=numbers[index]
    if element>maximum:
        maximum=element
    index=index+1
print(maximum)





# second maximum
a=[2,76,98,6,45,58,77]
i=0
max=a[0]
sec_max=a[0]
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
j=0
while j<len(a):
    if a[j]>sec_max and a[j]!=max:
        sec_max=a[j]
    j=j+1
print(sec_max)
