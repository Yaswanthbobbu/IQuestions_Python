a=0
b=1
n=5
count = 0
for i in range(1,n+1):
    count = a+b
    a = b
    b = count

print(count)
