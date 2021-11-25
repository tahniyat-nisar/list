a=["floor","cheese","carrot"]
index=0
while index<len(a):
    print(index,":",a[index])
    index=index+1

    
    
    
a=["python",25,3.0,True]
index=0
while index<len(a):   # or (len(a)-1) if you take then no need to take if condition
    # index=index+1
    if index==3:     #here we are trying to acess particular indexin element
        print(type(a[index]))
    index=index+1
