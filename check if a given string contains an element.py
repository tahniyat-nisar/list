a="https"+":"+"//www.w3resource.com/python-exercises/list/"
b=['.com', 'www', 'python']
i=0
while i<len(b):
    if b[i] in a:
        print(True)
    else:
        print(False)
    i=i+1
    
#  Output:True
#  ['.com', '.edu', '.tv']
# Output:False
