# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]]   # combined average of every element in main list
# sum=0
# i=0
# count=0
# while i<len(marks):
#     j=0
#     while j<len(marks[i]):
#         k=(marks[i][j])
#         sum=sum+k
#         count=count+1
#         j=j+1
#     i=i+1   
# print("Average of all the elements=",sum//count)




# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]]  #average of sublists containing equal lengths in main list
# i=0
# while i<len(marks):
#     j=0
#     sum=0
#     while j<len(marks[i]):
#         k=(marks[i][j])
#         sum=sum+k
#         j=j+1
#     i=i+1
#     print("Average of",i,"st","list in list=",sum//j)




# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]]       # Average of sublists containing decreasing lengths in main list
# i=0
# while i<len(marks):
#     j=0
#     sum=0
#     while j<len(marks[i]):
#         k=(marks[i][j])
#         sum=sum+k
#         j=j+1
#     i=i+1
#     print("Average of",i,"st","list in list=",sum//j)



marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]]   # Average of sublists containing different lengths in main list
i=0
while i<len(marks):
    j=0
    sum=0
    while j<len(marks[i]):
        k=(marks[i][j])
        sum=sum+k
        j=j+1
    i=i+1
    print("Average of",i,"st","sublist in Main list=",sum//j)







