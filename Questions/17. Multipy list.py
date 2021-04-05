listX=[1,2,3,4,5,6,7]

total = 1
for i in range(0,len(listX)):
    total = total*listX[i]
print(total)

import numpy
Mul=numpy.prod(listX)
print(Mul)
