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