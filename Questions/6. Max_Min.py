
# arr = [100,2,3,5,5]
#
# max = arr[0]
# n = len(arr)
#
# for i in range(1,n):
#     if arr[i]>max:
#         max= arr[i]
# print(max)

arr = [100,2,3,5,5]

min = arr[0]
n = len(arr)

for i in range(1,n):
    if arr[i]<min:
        min= arr[i]
print(min)