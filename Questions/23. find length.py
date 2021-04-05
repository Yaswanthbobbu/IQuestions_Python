str = "welcome to python"
print(len(str))

count=0
for i in range(0,len(str)):
    count+=1
print(count)

add=0
while str[add:]:
    add+=1
print(add)

temp = "X"
print((temp.join(str)).count(temp)+1)