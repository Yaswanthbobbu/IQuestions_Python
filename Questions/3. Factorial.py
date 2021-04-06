fact = 1
num1 = 5

for i in range(1,num1+1):
    fact = fact*i
print(fact)

n = 234
# def factorial(n):
#     if (n ==1 or n==0):
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(n))

# ternary approach

n= 10
def factorial(n):
    return 1 if (n==0 or n==1) else n * factorial(n-1)

