a= input("Enter number:" )
b=3

print(a , b)
# single line
a,b=b,a

print(a , b)

#using Temp variable
temp = a
a = b
b = temp

print(a , b)