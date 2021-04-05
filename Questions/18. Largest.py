listX=[1,2,3,4,5,6,7]

print(max(listX))
print(min(listX))

max = listX[3]
for i in range(0,len(listX)):
    if(max<listX[i]):
        max=listX[i]
print(max)

low = listX[2]
for i in range(0,len(listX)):
    if(low>listX[i]):
        low=listX[i]
print(low)

listX.sort()
print(listX[-2])
