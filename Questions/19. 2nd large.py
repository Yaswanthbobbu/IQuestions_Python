listX=[1,2,3,4,5,6,7]

listX.sort()
print(listX[-2])

# del listX[6:7]
# print(max(listX))

listX.remove(max(listX))
print(max(listX))