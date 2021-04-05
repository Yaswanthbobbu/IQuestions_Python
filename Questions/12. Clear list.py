# clear()
# del()
# * operator
# list with no value

list=[1,2,3,4,5]
list.clear()
print(list)

list=[1,2,3,4,5]
list=[]
print(list)

list=[1,2,3,4,5]
list*=0
print(list)


list=[1,2,3,4,5]
del list[1:3]
print(list)