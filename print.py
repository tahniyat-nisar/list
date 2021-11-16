# a=["floor","cheese","carrot"]
# index=0
# while index<len(a):
#     print(index,":",a[index])
#     index=index+1



# a=["python",25,3.0,True]
# index=0
# while index<len(a):
#     # index=index+1
#     if index==3:
#         print(type(a[index]))
#     index=index+1



# a=["python",25,3.0,True]
# i=0
# while i<len(a):
#     if type(a[i])==bool:
#         print(a[i])
#     i=i+1



# list1=[['g','f','g'],['i','s'],['b','e','s','t']]
# i=0
# sum=''
# while i<len(list1):
#     j=0
#     while j<len(list1[i]):
#         sum=sum+(list1[i][j])
#         j=j+1
#     i=i+1
# print(sum)










# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# i=1
# a=[]
# while i<len(n)/2:
#     j=0
#     while j<len(n):
#         if n[j]+n[i]==30:
#             t=[n[i],n[j]]
#             if t not in a:
#                 a.append(t)
#         j=j+1
#     i=i+1
# print(a)







# number = 30
# n = [10, 21,11, 12, 13, 14, 17, 18, 19,9]
# i=0
# y=[]
# while i<len(n):
#     j=0
#     while j<len(n):
#         if n[i]+n[j]==30:
#             x=((n[i],n[j]))
#             y.append(x)

#         j=j+1
#     i=i+1
# print(y)





# m = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]]
# sum=0
# i=0
# while i<len(m):
#     j=0
#     while j<len(m[i]):
#         k=(m[i][j])
#         sum=sum+k
#         j=j+1
#         print(sum)
#     i=i+1   
    

a=str(input("Enter a Number:"))
a=list(a)
b=0
while b<len(a):
    a[b]=int(a[b])**2
    b+=1
print(a)

















# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# i=0
# while i<len(n):
#     # print(n[i])
#     j=0
#     while j<len(n)-1:
       
#         # print(n[j])
#         count=0
#         while count>0:
#             if n[i]==n[j]:
#                 count=count+1
#                 if count==2:
#                     pass
#         j=j+1
#         print(n[j])
#     i=i+1












