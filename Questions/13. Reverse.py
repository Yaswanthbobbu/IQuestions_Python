list = [1,2,3,4,5]
# #reverse
# list.reverse()
# print(list)
#
# #slicing
# listR=list[::]
#print(listR)
print(len(list)-6)
for i in range(0,len(list)-1):
    n=list[i]
    list.insert(len(list)-i,n)
del list[0:4]
print(list)