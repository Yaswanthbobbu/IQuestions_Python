#slicing
listX=[1,2,3,4,5,6,7]
list1= listX[:]
print(list1)
#extend
list2=[]
list2.extend(listX)
print(list2)
#list method
list3=list(listX)
print(list3)
#copy method
list4=listX.copy()
print(list4)
#comprehensive method
list5=[i for i in listX]
print(list5)