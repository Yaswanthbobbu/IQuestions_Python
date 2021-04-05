list =[1,2,3,4]

#approach
list[0],list[2]=list[2],list[0]
print(list)
#tuple
get=(list[0],list[2])
list[2],list[0]=get
print(list)
#pop
pos1=list.pop(1)
pos2=list.pop(2)
list.insert(1,pos2)
list.insert(3,pos1)
print(list)
