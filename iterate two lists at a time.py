students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
counter = 0
while counter < length:
    print (students[counter] + str(marks[counter]))
    counter=counter+1

 
    
    
    
    
a=['0', '1', '2', '3', '4']
b=['red', 'green', 'black', 'blue', 'white']
c=['100', '200', '300', '400', '500']
i=0
e=[]
while i<len(a) and i<len(b) and i<len(c):
    d=(a[i]+b[i]+c[i])
    e.append(d)
    print(e)
    i=i+1
    
#   ['0red100', '1green200', '2black300', '3blue400', '4white500']
