list = [1,2,3,4,5,6]
n=4
flag=0
for i in range(0,len(list)-1):
    if i==n:
        print("No. is present")
        flag=1
        break
if flag==0:
        print("element not found")

#in operator
list = [1,2,3,4,5,6]
n=5
if(n in list):
    print("Element  found")
else:
    print('Element not found')
