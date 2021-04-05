mylist = [12,14,63,32,34,56,34,23,44]
size =len(mylist)

temp =mylist[0]
mylist[0]= mylist[size-1]
mylist[size-1]= temp

print(mylist)
#single statement
mylist[0],mylist[-1]=mylist[-1],mylist[0]
print(mylist)

#Tuple variable
get=(mylist[-1],mylist[0]) #packing
mylist[0],mylist[-1]=get
print(mylist)

# * Operand
start,*midle,end=mylist
mylist=[end,*midle,start]
print(mylist)

#pop method
first=mylist.pop(0)
last=mylist.pop(-1)

mylist.insert(0,last)
mylist.append(first)

print(mylist)

